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

    # Process the system first
    # If exists: update
    # Else: insert
    try:
        res = current_app.db.session.query(System).filter(System.systemname == systemname, System.username == username).first()
        if res is None:  # Insert
            new_system = System(systemname=systemname, username=username, description=description, method=method, results=json.dumps(results))
            current_app.db.session.add(new_system)
        else:  # Update
            current_app.db.session.query(System).filter(System.systemname == systemname) \
                .update({'description': description, 'method': method, 'results': json.dumps(results)})
        current_app.db.session.commit()

    except:
        current_app.logger.error("Error in inserting a new system:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN

    # Old components need to be substituted entirely
    try:
        # Delete old components
        current_app.db.session.query(Asset).filter(Asset.systemname == systemname).delete()
        current_app.db.session.query(Threat).filter(Threat.systemname == systemname).delete()
        current_app.db.session.query(Vulnerability).filter(Vulnerability.systemname == systemname).delete()

        # Add components
        for asset in assets:
            new_asset = Asset(systemname=systemname, assetname=asset['assetname'], val=asset['val'],
                              description=asset['description'])
            current_app.db.session.add(new_asset)
        for threat in threats:
            new_threat = Threat(systemname=systemname, threatname=threat['threatname'], val=threat['val'],
                                description=threat['description'])
            current_app.db.session.add(new_threat)
        for vul in vulnerabilities:
            new_vul = Vulnerability(systemname=systemname, vulname=vul['vulname'], val=vul['val'],
                                    description=vul['description'])
            current_app.db.session.add(new_vul)

        current_app.db.session.commit()
        return jsonify({'status': 0}), HTTP_OK

    except:
        current_app.logger.error("Error in inserting a new system:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN


@blueprint_sys.route('/query', methods=['GET'])
@error_guard('/sys/query')
@read_session
def sys_query_controller():
    username = session['username']
    systemname = request.args.get('systemname')
    if systemname is None:
        # Parameter error
        current_app.logger.error("Error in parsing requests:", exc_info=True)
        return jsonify({'status': 1, 'error': HTTP_BADREQ_TEXT}), HTTP_BADREQ

    try:
        res=current_app.db.session.query(System.systemname, System.username,System.method, System.results,
                                         System.description, System.createtime).filter(System.systemname == systemname, System.username == username).all()
        res1 = current_app.db.session.query(Asset.assetname,Asset.systemname,Asset.val,Asset.description).filter(Asset.systemname == systemname).all()
        res2 = current_app.db.session.query(Threat.threatname,Threat.systemname,Threat.val,Threat.description).filter(Threat.systemname == systemname).all()
        res3 = current_app.db.session.query(Vulnerability.vulname,Vulnerability.systemname,Vulnerability.val,Vulnerability.description).filter(Vulnerability.systemname == systemname).all()
        if len(res) == 0:
            return jsonify({'status': 1, 'error': '该系统不存在'}), HTTP_OK
        else:
            assets=[]
            for i in res1:
                temp = {'assetname':i[0],'val':i[2],'description':i[3]}
                assets.append(temp)
            threats=[]
            for i in res2:
                temp = {'threatname':i[0],'val':i[2],'description':i[3]}
                threats.append(temp)
            vulnerabilities=[]
            for i in res3:
                temp = {'vulname':i[0],'val':i[2],'description':i[3]}
                vulnerabilities.append(temp)
            return jsonify({'status': 0, 'description': res[0][4], 'method': res[0][2],
                            'assets': assets, 'threats': threats,
                            'vulnerabilities': vulnerabilities,'results': json.loads(res[0][3]), 'createtime': res[0][5]}), HTTP_OK

    except:
        current_app.logger.error("Error in querying a new system:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN


@blueprint_sys.route('/fetch_all', methods=['GET'])
@error_guard('/sys/fetch_all')
@read_session
def sys_fetch_all_controller():
    username = session['username']
    try:
        res = current_app.db.session.query(System.systemname, System.username, System.method, System.results,
                                           System.description, System.createtime).filter(System.username == username)\
                                           .all()
        if len(res) == 0:
            return jsonify({'status': 1, 'error': '您还没有测试任何系统'}), HTTP_OK
        else:
            systems = []
            for i in res:
                temp = {'systemname': i[0], 'method': i[2], 'results': json.loads(i[3]),
                        'description': i[4], 'createtime': i[5]}
                systems.append(temp)
            return jsonify({'status': 0, 'systems': systems}), HTTP_OK

    except:
        current_app.logger.error("Error in fetching systems:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN


@blueprint_sys.route('/delete', methods=['DELETE'])
@error_guard('/sys/delete')
@read_session
def sys_delete_controller():
    username = session['username']
    try:
        temp_data = request.json
        systemname = temp_data['systemname']
    except:  # Parameter error
        current_app.logger.error("Error in parsing requests:", exc_info=True)
        return jsonify({'status': 1, 'error': HTTP_BADREQ_TEXT}), HTTP_BADREQ

    try:
        system = current_app.db.session.query(System).filter(System.systemname == systemname).first()
        # Check whether this systemname is existed
        if system:
            current_app.db.session.query(System).filter(System.systemname == systemname, System.username == username).delete()
            return jsonify({'status': 0}), HTTP_OK
        else:
            return jsonify({'status': 1, 'error': '系统不存在'}), HTTP_OK

    except:
        current_app.logger.error("Error in deleting a new system:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN



