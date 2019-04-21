import hashlib
from functools import wraps
from flask import current_app, jsonify, session
from params import HTTP_UNKNOWN, HTTP_UNAUTH


# Handle cookies: check for invalid users
def read_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            assert session['username']
        except KeyError:
            return jsonify({'error': 'Cookie不能通过验证！'}), HTTP_UNAUTH

        res = func(*args, **kwargs)
        return res

    return wrapper


# Handle unexpected errors
def error_guard(domain):
    # domain: string(something like a function name?)
    def wrapper_out(func):
        @wraps(func)
        def wrapper_in(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                if len(res) > 1:  # Save http codes(if have one)
                    current_app.logger.info('Request completed on ' + domain + ' with code ' + str(res[1]))
                return res
            except:
                current_app.logger.error('Raise error on ' + domain + ' : ', exc_info=True)
                # Just don't feel like returning a server internal error(500)
                return jsonify({'error': '请求发生了未知错误'}), HTTP_UNKNOWN

        return wrapper_in

    return wrapper_out


# Default hash method
def md5(string):
    return hashlib.md5(string.encode("utf8")).hexdigest()
