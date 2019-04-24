from models import User
from server import app
from params import HTTP_OK, HTTP_UNKNOWN, HTTP_BADREQ, HTTP_UNAUTH


class TestModels(object):
    def setup_class(self):
        # Init
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def teardown_class(self):
        # Delete users
        self.app.db.session.query(User).filter(User.username == '__test__user').delete()
        self.app.db.session.commit()
        # Close connections
        self.app.db.session.remove()
        print('\n/auth/register ut complete!')

    # Test for bad requests
    def test_400(self):
         res = self.client.post('/auth/register', json={'username': 'test'})
         assert res.status_code == HTTP_BADREQ


    # Test for successful register is a sub-test of
    # the test for duplicate users
    def test_exist(self):
        # Valid
        res = self.client.post('/auth/register', json={'username': '__test__user', 'password': '123456'})
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 0

        # Invalid
        res = self.client.post('/auth/register', json={'username': '__test__user', 'password': '654321'})
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 1
        assert data['error'] == '用户名已被注册'
