import json
from jsonapi.app import app
from jsonapi.tests.constants import default_request
from jsonapi.facades.UserFacade import UserFacade
from jsonapi.facades.MessageFacade import MessageFacade


def test_fuzzy_search_users():
    UserFacade.delete_all()
    MessageFacade.delete_all()

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

    john_id = None
    jenny_id = None

    with app.test_client() as c:
        for user in users:
            resp = c.put('/api/user', data=json.dumps(user), **default_request)

            data = json.loads(resp.data)

            assert isinstance(data, dict)
            assert 'username' in data
            assert 'email' in data
            assert 'password' in data

            if data['username'] == 'john.doe41':
                john_id = data['id']

            if data['username'] == 'jenny.cool':
                jenny_id = data['id']

    messages_from_jenny_to_john = [
        {
            'message': 'hi john, I love you',
            'sender': jenny_id,
            'receiver': john_id
        },
        {
            'message': 'why are you not answering my texts?',
            'sender': jenny_id,
            'receiver': john_id
        }
    ]

    messages_from_john_to_jenny = [
        {
            'message': 'I cant talk with you anymore',
            'sender': john_id,
            'receiver': jenny_id
        }
    ]

    messages = messages_from_jenny_to_john + messages_from_john_to_jenny

    with app.test_client() as c:
        for msg in messages:
            resp = c.put(
                '/api/message',
                data=json.dumps(msg),
                **default_request
            )

            data = json.loads(resp.data)

            assert 'message' in data
            assert 'sender' in data
            assert 'receiver' in data
            assert 'id' in data

    with app.test_client() as c:
        for msg in messages:
            resp = c.get(
                '/api/message/{}/sent'.format(jenny_id),
                **default_request
            )

            data = json.loads(resp.data)

            assert isinstance(data, list)
            assert len(data) == 2

    with app.test_client() as c:
        for msg in messages:
            resp = c.get(
                '/api/message/{}/received'.format(jenny_id),
                **default_request
            )

            data = json.loads(resp.data)

            assert isinstance(data, list)
            assert len(data) == 1

    with app.test_client() as c:
        for msg in messages:
            resp = c.get(
                '/api/message/{}/received'.format(john_id),
                **default_request
            )

            data = json.loads(resp.data)

            assert isinstance(data, list)
            assert len(data) == 2
