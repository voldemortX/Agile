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
        temp_data = request.json
        username = temp_data['username']
        password = temp_data['password']
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

    return jsonify({'status': 0}), HTTP_OK


@blueprint_auth.route('/login', methods=['POST'])
@error_guard('/auth/login')
def auth_login_controller():
    # Get post parameters
    try:
        temp_data = request.json
        username = temp_data['username']
        password = temp_data['password']
    except:  # Parameter error
        current_app.logger.error("Error in parsing requests:", exc_info=True)
        return jsonify({'status': 1, 'error': HTTP_BADREQ_TEXT}), HTTP_BADREQ

    user=User.query.filter(User.username == username).first()
    pwd=md5(password)
    # Check whether this username is existed
    if user:
        #Check the password
        if user.username==username and user.password==pwd:
            return jsonify({'status': 0}), HTTP_OK
        else:
            return jsonify({'status': 1, 'error': '用户名或密码输入错误'}), HTTP_OK
    else:
        return jsonify({'status': 1, 'error': '用户名不存在！'}), HTTP_OK
