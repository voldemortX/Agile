#!/usr/bin/env python
# -*- coding:utf-8 -*-
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

    def teardown_class(self):
        # Deletes(cascade)
        self.app.db.session.query(User).filter(User.username == '__test__user').delete()
        self.app.db.session.commit()
        # Close connections
        self.app.db.session.remove()
        print('\n/sys/delete ut complete!')

    def test_systems(self):
        # Add a system(column 'createtime' is automated)
        new_system = System(systemname='__test__system', username='__test__user',
                            method='__test__method', results=json.dumps([{'attr': 'val'}]),
                            description='test')
        self.app.db.session.add(new_system)
        self.app.db.session.commit()
        res = self.app.db.session.query(System.results).filter(System.systemname == '__test__system').first()
        assert json.loads(res[0]) == [{'attr': 'val'}]

    # Test for wrong cookies
    def test_401(self):
        res = self.client.delete('/sys/delete?systemname=__test__system2')
        assert res.status_code == HTTP_UNAUTH

    # Test for bad requests
    def test_400(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = '__test__user'
        res = self.client.delete('/sys/delete?username=__test__user')
        assert res.status_code == HTTP_BADREQ

    def test_exist(self):
        # Invalid
        res = self.client.delete('/sys/delete?systemname=__test__system2')
        assert res.status_code == HTTP_OK
        assert res.is_json is True
        data = res.get_json()
        assert data['status'] == 1
        assert data['error'] == '系统不存在'

        # Valid
        with self.client as c:
            res = self.client.delete('/sys/delete?systemname=__test__system')
            assert res.status_code == HTTP_OK
            assert res.is_json is True
            data = res.get_json()
            assert data['status'] == 0

