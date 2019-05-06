from models import *
from params import appConfig
from flask import Flask
import json

# Test models.py by pytest
# Search for class names start with 'Test',
# method names start with 'test_'


# These 3 tests are to be run together
class TestModels(object):
    def setup_class(self):
        # Init
        self.app = Flask(__name__)
        self.app.config.from_mapping(appConfig)
        self.app.db = SQLAlchemy(self.app)

    def teardown_class(self):
        # Close connections
        self.app.db.session.remove()
        print('\nmodels.py ut complete!')

    # Use table users as an example for basic tests
    def test_users(self):
        # All has SELECT
        # INSERT
        new_user = User(username='__test__admin', password='123456')
        self.app.db.session.add(new_user)
        self.app.db.session.commit()
        res = self.app.db.session.query(User.username, User.password).filter(User.username == '__test__admin').first()
        assert res[0] == '__test__admin'
        assert res[1] == '123456'

        # UPDATE
        self.app.db.session.query(User.username, User.password).filter(User.username == '__test__admin') \
            .update({'password': ''})
        self.app.db.session.commit()
        res = self.app.db.session.query(User.password).filter(User.username == '__test__admin').first()
        assert res[0] == ''

    # Test for default values and JSON strings
    def test_systems(self):
        # Add a system(column 'createtime' is automated)
        new_system = System(systemname='__test__system', username='__test__admin',
                            method='相乘法1', results=json.dumps([{'attr': 'val'}]),
                            description='test')
        self.app.db.session.add(new_system)
        self.app.db.session.commit()
        res = self.app.db.session.query(System.results).filter(System.systemname == '__test__system').first()
        assert json.loads(res[0]) == [{'attr': 'val'}]

    # Test cascade DELETE by foreign keys
    # e.g. If you delete a system, it's assets&threats&vulnerabilities are gone as well
    # Respectively, if you delete an user, it's systems&everything in these systems are gone as well
    # So actually, only testing user deletions is enough
    def test_cascade(self):
        # Add assets&threats&vulnerabilities
        new_asset = Asset(assetname='__test__asset', systemname='__test__system',
                          val=5, description='test')
        self.app.db.session.add(new_asset)
        new_threat = Threat(threatname='__test__threat', systemname='__test__system',
                            val=4, description='test')
        self.app.db.session.add(new_threat)
        new_vulnerability = Vulnerability(vulname='__test__vul', systemname='__test__system',
                                          val=3, description='test')
        self.app.db.session.add(new_vulnerability)
        self.app.db.session.commit()

        # DELETE
        self.app.db.session.query(User).filter(User.username == '__test__admin').delete()
        self.app.db.session.commit()
        res = self.app.db.session.query(System).filter(System.username == '__test__admin').first()
        assert res is None
        res = self.app.db.session.query(Asset).filter(Asset.systemname == '__test__system').first()
        assert res is None
        res = self.app.db.session.query(Threat).filter(Threat.systemname == '__test__system').first()
        assert res is None
        res = self.app.db.session.query(Vulnerability).filter(Vulnerability.systemname == '__test__system').first()
        assert res is None
