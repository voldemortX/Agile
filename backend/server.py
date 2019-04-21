import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from params import appConfig
from myLog import init_logger, log_path
from controllers.auth import blueprintAuth

app = Flask(__name__)
app.config.from_mapping(appConfig)
app.db = SQLAlchemy(app)
app.register_blueprint(blueprintAuth)


@app.teardown_request
def checkin_db(exc):
    try:
        # Shutdown idle database sessions
        app.db.session.remove()
    except AttributeError:
        pass


if __name__ == '__main__':
    # Start the logging system
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    init_logger(app)

    # Start the web server
    app.run('0.0.0.0', port=7777)
