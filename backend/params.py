# HTTP status codes
HTTP_OK = 200
HTTP_UNKNOWN = 520
HTTP_BADREQ = 400
HTTP_BADREQ_TEXT = 'Wrong parameters!'
HTTP_UNAUTH = 401


# Flask app parameters
secretKey = b"/[\xec\nabcde'L2x76_"  # Session key
appConfig = {
                'SECRET_KEY': secretKey,
                'DEBUG': False,
                'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:fshm0113@localhost:3306/agile'
            }
