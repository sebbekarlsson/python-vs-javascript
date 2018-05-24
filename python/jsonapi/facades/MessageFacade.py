from jsonapi.entities.Message import Message
from jsonapi.db import DB


COLUMN = 'message'


class MessageFacade(object):

    @staticmethod
    def create(**kwargs):
        message = Message(**kwargs)

        return Message(**DB.insert_document(COLUMN, message.export()))

    @staticmethod
    def delete_all():
        return DB.delete_all_documents(column=COLUMN)

    @staticmethod
    def get_by(**kwargs):
        return DB.get_documents_by(COLUMN, **kwargs)
