import json
from jsonapi.app import app
from jsonapi.tests.constants import default_request


def test_register_user():
    user = {
        'username': 'john.doe55',
        'email': 'john.doe@doecompany.com',
        'password': 'bad_password24'
    }

    with app.test_client() as c:
        resp = c.put('/api/user', data=json.dumps(user), **default_request)

        data = json.loads(resp.data)

        assert isinstance(data, dict)
        assert 'username' in data
        assert 'email' in data
        assert 'password' in data

        resp = c.put('/api/user', data=json.dumps(user), **default_request)

        data = json.loads(resp.data)

        assert 'errors' in data
