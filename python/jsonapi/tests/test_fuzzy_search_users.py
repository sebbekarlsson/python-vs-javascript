import json
from jsonapi.app import app
from jsonapi.tests.constants import default_request
from jsonapi.facades.UserFacade import UserFacade


def test_fuzzy_search_users():
    UserFacade.delete_all()

    users = [
        {
            'username': 'john.doe41',
            'email': 'john.doe@doecompany.com',
            'password': 'bad_password24'
        },
        {
            'username': 'jenny.cool',
            'email': 'jenny@doecompany.com',
            'password': 'bad_password24'
        },
        {
            'username': 'thomas.cool',
            'email': 'thomas@doecompany.com',
            'password': 'bad_password24'
        },
        {
            'username': 'pinkfloydlover',
            'email': 'pink@doecompany.com',
            'password': 'bad_password24'
        }
    ]

    with app.test_client() as c:
        for user in users:
            resp = c.put('/api/user', data=json.dumps(user), **default_request)

            data = json.loads(resp.data)

            assert isinstance(data, dict)
            assert 'username' in data
            assert 'email' in data
            assert 'password' in data

    with app.test_client() as c:
        query = {'email': '@doe'}
        resp = c.get('/api/user?q=' + json.dumps(query), **default_request)
        data = json.loads(resp.data)

        assert len(data) == 4

        query = {'username': 'jen'}
        resp = c.get('/api/user?q=' + json.dumps(query), **default_request)
        data = json.loads(resp.data)

        assert len(data) == 1
