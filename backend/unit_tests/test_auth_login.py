#!/usr/bin/env python 
# -*- coding:utf-8 -*-
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
        print('\n/auth/login ut complete!')


    def test_exist(self):
        # Invalid
        res = self.client.post('/auth/login', json={'username': '__test__user', 'password': '654321'})
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 1
        assert data['error'] == '用户名不存在！'

        res = self.client.post('/auth/login', json={'username': '__test__user1', 'password': '12345'})
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 1
        assert data['error'] == '用户名或密码输入错误'

        # Valid
        res = self.client.post('/auth/login', json={'username': '__test__user1', 'password': '123'})
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 0