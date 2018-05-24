import json
from jsonapi.config import config
from jsonapi.random_utils import get_random_string


class DB(object):

    @staticmethod
    def get_database():
        with open(config['database'], 'r+') as _file:
            data = _file.read()
        _file.close()

        return json.loads(data) if data else {}

    @staticmethod
    def get_documents_by_like(column, **kwargs):
        data = DB.get_database()
        entities = []

        if column in data:
            for entity in data[column]:
                for k, v in dict(**kwargs).items():
                    if k not in entity:
                        continue

                    if v.lower() in entity[k].lower():
                        entities.append(entity)

        return entities

    @staticmethod
    def get_documents_by(column, **kwargs):
        data = DB.get_database()
        entities = []

        if column in data:
            for entity in data[column]:
                for k, v in dict(**kwargs).items():
                    if k not in entity:
                        continue

                    if entity[k] == v:
                        entities.append(entity)

        return entities

    @staticmethod
    def get_document_by(column, **kwargs):
        entities = DB.get_documents_by(column, **kwargs)

        return entities[0] if entities else None

    @staticmethod
    def insert_document(column, document):
        data = DB.get_database()

        if column not in data:
            data[column] = []

        if not DB.get_document_by(column, id=document['id']):
            document['id'] = get_random_string(24)
            data[column].append(document)
        else:
            raise Exception('Document with id: {} already exists'.format(
                document['id']
            ))

        with open(config['database'], 'w+') as _file:
            _file.write(json.dumps(data))
        _file.close()

        return document

    @staticmethod
    def delete_all_documents(column=None):
        data = DB.get_database()

        if column:
            data[column] = []
        else:
            data = {}

        with open(config['database'], 'w+') as _file:
            _file.write(json.dumps(data))
        _file.close()

        return data
