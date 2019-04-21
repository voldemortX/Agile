from utils import error_guard, md5
from params import HTTP_BADREQ, HTTP_BADREQ_TEXT, HTTP_UNKNOWN, HTTP_OK
from flask import current_app, jsonify, request, session, Blueprint
from models import User
from controllers.common import find_user_by_username

blueprint_auth = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint_auth.route('/register', methods=['POST'])
@error_guard('/auth/register')
def auth_register_controller():
    # Get post parameters
    try:
        tempData = request.json
        username = tempData['username']
        password = tempData['password']
    except:  # Parameter error
        current_app.logger.error("Error in parsing requests:", exc_info=True)
        return jsonify({'status': 1, 'error': HTTP_BADREQ_TEXT}), HTTP_BADREQ

    # Check whether this username is already registered
    temp = find_user_by_username(username)
    if temp == 1:
        return jsonify({'status': 1, 'error': '用户名已被注册'}), HTTP_OK
    elif temp == 2:
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN

    # Store user
    try:
        new_user = User(username=username, password=md5(password))
        current_app.db.session.add(new_user)
        current_app.db.session.commit()
    except:
        current_app.logger.error("Error in inserting a new user:", exc_info=True)
        current_app.db.session.rollback()
        return jsonify({'status': 1, 'error': '数据库未知错误'}), HTTP_UNKNOWN


@blueprint_auth.route('/login', methods=['POST'])
@error_guard('/auth/login')
def auth_login_controller():
    pass
