from utils import error_guard, read_session
from params import HTTP_BADREQ, HTTP_BADREQ_TEXT, HTTP_UNKNOWN, HTTP_OK
from flask import current_app, jsonify, request, session, Blueprint
import requests
import json

blueprintAuth = Blueprint('auth', __name__, url_prefix='/auth')


@blueprintAuth.route('/register', methods=['POST'])
@error_guard('/auth/register')
def auth_register_controller():
    pass
