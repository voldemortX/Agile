from utils import error_guard, read_session
from params import HTTP_BADREQ, HTTP_BADREQ_TEXT, HTTP_UNKNOWN, HTTP_OK
from flask import current_app, jsonify, request, session, Blueprint
import requests
import json

blueprint_sys = Blueprint('sys', __name__, url_prefix='/sys')


@blueprint_sys.route('/submit', methods=['POST'])
@error_guard('/sys/submit')
@read_session
def sys_submit_controller():
    pass


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
