from models import *
from server import app
from params import HTTP_OK, HTTP_UNKNOWN, HTTP_BADREQ, HTTP_UNAUTH
import json

# Doesn't seem possible to have a invalid request?


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
        print('\n/sys/submit ut complete!')

    # Test for bad requests
    def test_400(self):
        data = {'systemname': '', 'description': '', 'method': '',
                'assets': [], 'vulnerabilities': [], 'threats': [], 'results': []}
        params = list(data.keys())
        for param in params:
            temp = data
            temp.pop(param)
            res = self.client.post('/sys/submit', json=temp)
            assert res.status_code == HTTP_BADREQ

    # Test for brand new systems
    def test_new(self):
        temp = {'systemname': '__test__system2', 'description': 'xxx', 'method': '相乘法',
                'assets': [{'assetname': '__test__asset', 'description': 'xxx', 'val': 1}],
                'vulnerabilities': [{'vulname': '__test__vul', 'description': 'xxx', 'val': 1}],
                'threats': [{'threatname': '__test__threat', 'description': 'xxx', 'val': 1}],
                'results': [{'attr1': 'val1'}, {'attr2': 'val2'}]}
        res = self.client.post('/sys/submit', json=temp)
        assert res.status_code == 200
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 0

        temp['systemname'] = '__test__system'
        res = self.client.post('/sys/submit', json=temp)
        assert res.status_code == 200
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 0

    # Test for a system update
    def test_old(self):
        temp = {'systemname': '__test__system2', 'description': 'xxx', 'method': '相乘法',
                'assets': [{'assetname': '__test__asset2', 'description': 'xxx', 'val': 1}],
                'vulnerabilities': [{'vulname': '__test__vul', 'description': 'yyy', 'val': 1}],
                'threats': [{'threatname': '__test__threat', 'description': 'xxx', 'val': 3}],
                'results': [{'attr1': 'val3'}, {'attr2': 'val2'}]}
        res = self.client.post('/sys/submit', json=temp)
        assert res.status_code == 200
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 0

    # Testing data in DB
    def test_data(self):
        # Correct systems
        res = self.app.db.session.query(System.systemname, System.results) \
            .filter((System.systemname == '__test__system') | (System.systemname == '__test__system2')).all()
        assert len(res) == 2
        for system in res:
            if system[0] == '__test__system2':
                assert json.loads(system[1]) == [{'attr1': 'val3'}, {'attr2': 'val2'}]
            else:
                assert json.loads(system[1]) == [{'attr1': 'val1'}, {'attr2': 'val2'}]

        # Correct updated components
        res = self.app.db.session.query(Asset.assetname).filter(Asset.systemname == '__test__system2').all()
        assert len(res) == 1
        assert res[0][0] == '__test__asset2'
        res = self.app.db.session.query(Asset.assetname).filter(Asset.systemname == '__test__system').all()
        assert len(res) == 1
        assert res[0][0] == '__test__asset'
        res = self.app.db.session.query(Vulnerability.description).filter(Vulnerability.systemname == '__test__system2').first()
        assert res[0] == 'yyy'
        res = self.app.db.session.query(Threat.val).filter(Threat.systemname == '__test__system2').first()
        assert res[0] == 3
