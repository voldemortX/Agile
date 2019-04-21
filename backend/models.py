from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
The table name is automatically set for you unless overridden.
It’s derived from the class name converted to lowercase
and with “CamelCase” converted to “camel_case”.
To override the table name, set the __tablename__ class attribute.
'''

# Table declarations
