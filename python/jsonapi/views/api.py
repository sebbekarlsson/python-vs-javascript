from flask import Blueprint, jsonify, request
import json
from jsonapi.password import get_hashed_password
from jsonapi.facades.UserFacade import UserFacade
from jsonapi.facades.MessageFacade import MessageFacade
from jsonapi.exceptions import FieldNotUniqueException


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


@bp.route('/user', methods=['PUT'])
def register_user():
    errors = []
    data = request.get_json()

    username = data['username']
    email = data['email']
    password = data['password']

    try:
        user = UserFacade.create(
            username=username,
            email=email,
            password=get_hashed_password(password)
        )
    except FieldNotUniqueException as e:
        errors.append(e.message)

    if errors:
        return jsonify({'errors': errors}), 400

    return jsonify(user.export())


@bp.route('/user', methods=['GET'])
def fuzzy_search_users():
    data = json.loads(request.args.get('q')) if request.args.get('q') else {}

    return jsonify(UserFacade.fuzzy_search(**data))


@bp.route('/message', methods=['PUT'])
def send_message_to_user():
    data = request.get_json()

    message = MessageFacade.create(**data)

    return jsonify(message.export())


@bp.route('/message/<user_id>/sent', methods=['GET'])
def fetch_user_sent_messages(user_id):
    return jsonify(MessageFacade.get_by(sender=user_id))


@bp.route('/message/<user_id>/received', methods=['GET'])
def fetch_user_received_messages(user_id):
    return jsonify(MessageFacade.get_by(receiver=user_id))
