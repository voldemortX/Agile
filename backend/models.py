from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# The table name is automatically set for you unless overridden.
# It’s derived from the class name converted to lowercase
# and with “CamelCase” converted to “camel_case”.
# To override the table name, set the __tablename__ class attribute.
#
# Table declarations:


class Asset(db.Model):
    __tablename__ = 'assets'

    assetname = db.Column(db.String(20), primary_key=True, nullable=False)
    systemname = db.Column(db.ForeignKey('systems.systemname', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    val = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    system = db.relationship('System', primaryjoin='Asset.systemname == System.systemname', backref='assets')


class System(db.Model):
    __tablename__ = 'systems'

    systemname = db.Column(db.String(50), primary_key=True, nullable=False)
    username = db.Column(db.ForeignKey('users.username', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    method = db.Column(db.String(20), nullable=False)
    results = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    user = db.relationship('User', primaryjoin='System.username == User.username', backref='systems')


class Threat(db.Model):
    __tablename__ = 'threats'

    threatname = db.Column(db.String(20), primary_key=True, nullable=False)
    systemname = db.Column(db.ForeignKey('systems.systemname', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    val = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    system = db.relationship('System', primaryjoin='Threat.systemname == System.systemname', backref='threats')


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(40), nullable=False)


class Vulnerability(db.Model):
    __tablename__ = 'vulnerabilities'

    vulname = db.Column(db.String(20), primary_key=True, nullable=False)
    systemname = db.Column(db.ForeignKey('systems.systemname', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    val = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    system = db.relationship('System', primaryjoin='Vulnerability.systemname == System.systemname', backref='vulnerabilities')

