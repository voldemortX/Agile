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
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = '__test__user'

    def test_systems(self):
        # Add a system(column 'createtime' is automated)
        new_system = System(systemname='__test__system', username='__test__user',
                            method='__test__method', results=json.dumps([{'attr': 'val'}]),description='test')
        self.app.db.session.add(new_system)
        self.app.db.session.commit()
        res = self.app.db.session.query(System.results).filter(System.systemname == '__test__system').first()
        assert json.loads(res[0]) == [{'attr': 'val'}]
        # Add a asset
        new_asset = Asset(assetname='__test__asset', systemname='__test__system',val='10',  description='testa')
        self.app.db.session.add(new_asset)
        self.app.db.session.commit()
        # Add a threat
        new_threat = Threat(threatname='__test__threat', systemname='__test__system', val='20', description='testt')
        self.app.db.session.add(new_threat)
        self.app.db.session.commit()
        # Add a vul
        new_vul = Vulnerability(vulname='__test__vul', systemname='__test__system', val='30',description='testv')
        self.app.db.session.add(new_vul)
        self.app.db.session.commit()

    def teardown_class(self):
        # Deletes(cascade)
        self.app.db.session.query(User).filter(User.username == '__test__user').delete()
        self.app.db.session.commit()
        self.app.db.session.query(System).filter(System.username == '__test__user').delete()
        self.app.db.session.commit()
        self.app.db.session.query(Asset).filter(Asset.systemname == '__test__system').delete()
        self.app.db.session.commit()
        self.app.db.session.query(Threat).filter(Threat.systemname == '__test__system').delete()
        self.app.db.session.commit()
        self.app.db.session.query(Vulnerability).filter(Vulnerability.systemname == '__test__system').delete()
        self.app.db.session.commit()
        # Close connections
        self.app.db.session.remove()
        print('\n/sys/query ut complete!')

    def test_exist(self):
        # Invalid
        res = self.client.get('/sys/query?systemname=__test__system2')
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 1
        assert data['error'] == '该系统不存在'

        # Valid
        with self.client as c:
            res = self.client.get('/sys/query?systemname=__test__system')
            assert res.status_code == HTTP_OK
            assert res.is_json is True
            data = res.get_json()
            assert data['status'] == 0

