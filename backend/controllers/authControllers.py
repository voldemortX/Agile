from utils import error_guard, read_session
from params import HTTP_BADREQ, HTTP_BADREQ_TEXT, HTTP_UNKNOWN, HTTP_OK
from flask import current_app, jsonify, request, session, Blueprint
import requests

blueprint_auth = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint_auth.route('/register', methods=['POST'])
@error_guard('/auth/register')
def auth_register_controller():
    pass


@blueprint_auth.route('/login', methods=['POST'])
@error_guard('/auth/login')
def auth_login_controller():
    pass
