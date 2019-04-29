from utils import error_guard, read_session
from params import HTTP_BADREQ, HTTP_BADREQ_TEXT, HTTP_UNKNOWN, HTTP_OK
from flask import current_app, jsonify, request, session, Blueprint
from models import *
import json

blueprint_sys = Blueprint('sys', __name__, url_prefix='/sys')


@blueprint_sys.route('/submit', methods=['POST'])
@error_guard('/sys/submit')
@read_session
def sys_submit_controller():
    username = session['username']
    # Get post parameters
    try:
        temp_data = request.json
        systemname = temp_data['systemname']
        description = temp_data['description']
        method = temp_data['method']
        assets = temp_data['assets']
        vulnerabilities = temp_data['vulnerabilities']
        threats = temp_data['threats']
        results = temp_data['results']
    except:  # Parameter error
        current_app.logger.error("Error in parsing requests:", exc_info=True)
        return jsonify({'status': 1, 'error': HTTP_BADREQ_TEXT}), HTTP_BADREQ

    # If exists: update
    # Else: insert
    try:
        res = current_app.db.session.query(System).filter(System.systemname == systemname).first()
        if res is None:  # Insert
            # Add the system first
            new_system = System(systemname=systemname, username=username, description=description, method=method, results=json.dumps(results))
            current_app.db.session.add(new_system)
            # Add components
            for asset in assets:
                new_asset = Asset(systemname=systemname, assetname=asset['assetname'], val=asset['val'], description=asset['description'])
                current_app.db.session.add(new_asset)
            for threat in threats:
                new_threat = Threat(systemname=systemname, threatname=threat['threatname'], val=threat['val'], description=threat['description'])
                current_app.db.session.add(new_threat)
            for vul in vulnerabilities:
                new_vul = Vulnerability(systemname=systemname, vulname=vul['vulname'], val=vul['val'], description=vul['description'])
                current_app.db.session.add(new_vul)
        else:  # Update
            # Update the system first
            current_app.db.session.query(System).filter(System.systemname == systemname) \
                .update({'description': description, 'method': method, 'results': json.dumps(results)})
            # Query components
            old_assets = current_app.db.session.query(Asset.assetname).filter(Asset.systemname == systemname).all()
            old_threats = current_app.db.session.query(Threat.threatname).filter(Threat.systemname == systemname).all()
            old_vuls = current_app.db.session.query(Vulnerability.vulname).filter(Vulnerability.systemname == systemname).all()
            # Process components
            insert_or_update_components(old_comps=old_assets, new_comps=assets, col_name='assetname', table_class=Asset, systemname=systemname)
            insert_or_update_components(old_comps=old_threats, new_comps=threats, col_name='threatname', table_class=Threat, systemname=systemname)
            insert_or_update_components(old_comps=old_vuls, new_comps=vulnerabilities, col_name='vulname', table_class=Vulnerability, systemname=systemname)

        current_app.db.session.commit()
        return jsonify({'status': 0}), HTTP_OK

    except:
        current_app.logger.error("Error in inserting a new user:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN


@blueprint_sys.route('/query', methods=['GET'])
@error_guard('/sys/query')
@read_session
def sys_query_controller():
    pass


@blueprint_sys.route('/fetch_all', methods=['GET'])
@error_guard('/sys/fetch_all')
@read_session
def sys_fetch_all_controller():
    pass


@blueprint_sys.route('/delete', methods=['DELETE'])
@error_guard('/sys/delete')
@read_session
def sys_delete_controller():
    pass


# Update old components / Insert
def insert_or_update_components(old_comps, new_comps, col_name, table_class, systemname):
    for new_comp in new_comps:
        flag = True  # Insertion flag
        for old_comp in old_comps:
            if old_comp[0] == new_comp[col_name]:
                current_app.db.session.query(table_class).filter(Asset.assetname == new_comp[col_name]) \
                    .update({'val': new_comp['val'], 'description': new_comp['description']})
                flag = False
                break
        if flag:
            temp = table_class(systemname=systemname, assetname=new_comp[col_name], val=new_comp['val'], description=new_comp['description'])
            current_app.db.session.add(temp)