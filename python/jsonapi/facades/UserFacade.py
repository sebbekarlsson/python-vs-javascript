from jsonapi.entities.User import User
from jsonapi.db import DB
from jsonapi.exceptions import FieldNotUniqueException


COLUMN = 'user'


class UserFacade(object):

    @staticmethod
    def create(**kwargs):
        user = User(**kwargs)

        if DB.get_document_by(COLUMN, username=user.username):
            raise FieldNotUniqueException('user.username neads to be unique')

        return User(**DB.insert_document(COLUMN, user.export()))

    @staticmethod
    def delete_all():
        return DB.delete_all_documents(column=COLUMN)

    @staticmethod
    def fuzzy_search(**kwargs):
        return DB.get_documents_by_like(COLUMN, **kwargs)
