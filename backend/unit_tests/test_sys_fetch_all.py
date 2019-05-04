from models import *
from server import app
from params import HTTP_OK, HTTP_UNKNOWN, HTTP_BADREQ, HTTP_UNAUTH
import json


class TestModels(object):
    def setup_class(self):
        # Init
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()
        # Add an user for testing
        new_user = User(username='__test__user', password='xxx')
        self.app.db.session.add(new_user)
        self.app.db.session.commit()
        # Set pseudo cookies
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = '__test__user'

    def teardown_class(self):
        # Deletes(cascade)
        self.app.db.session.query(User).filter(User.username == '__test__user').delete()
        self.app.db.session.commit()
        # Close connections
        self.app.db.session.remove()
        print('\n/sys/fetch_all ut complete!')

    def test_invalid(self):
        # Invalid
        res = self.client.get('/sys/fetch_all')
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 1
        assert data['error'] == '您还没有测试任何系统'

    def test_valid(self):
        #Valid
        # Add a system(column 'createtime' is automated)
        new_system = System(systemname='__test__system', username='__test__user',
                            method='__test__method', results=json.dumps([{'attr': 'val'}]),
                            description='test')
        self.app.db.session.add(new_system)
        self.app.db.session.commit()
        res = self.app.db.session.query(System.results).filter(System.systemname == '__test__system').first()
        assert json.loads(res[0]) == [{'attr': 'val'}]

        res = self.client.get('/sys/fetch_all')
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 0



