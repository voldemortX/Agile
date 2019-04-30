from models import *
from server import app
from params import HTTP_OK, HTTP_UNKNOWN, HTTP_BADREQ, HTTP_UNAUTH


class TestModels(object):
    def setup_class(self):
        # Init
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()
        # Set pseudo cookies
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = '__test__username'

    def teardown_class(self):
        # Deletes
        #self.app.db.session.query(System).filter(System.systemname == '__test__system').delete()
        #self.app.db.session.commit()
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

