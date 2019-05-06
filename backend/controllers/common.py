from flask import current_app
from models import User


# If username exists, return 1, otherwise 0
# Return 2 for unexpected errors
def find_user_by_username(username):
    try:
        res = current_app.db.session.query(User).filter(User.username == username).first()
        if res is None:
            return 0
        else:
            return 1
    except:
        current_app.logger.error("Error in finding users:", exc_info=True)
        return 2
