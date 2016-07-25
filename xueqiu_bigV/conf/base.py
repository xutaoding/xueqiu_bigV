from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, OperationFailure

from .config import BIGV_HOST, BIGV_PORT, BIGV_DB, BIGV_CUBES, BIGV_USR


class BaseConfig(object):
    def __init__(self):
        self.client = MongoClient(BIGV_HOST, BIGV_PORT)
        self.user = self.client[BIGV_DB][BIGV_USR]
        self.cubes = self.client[BIGV_DB][BIGV_CUBES]

    @staticmethod
    def create_unique_index(collection, field):
        try:
            indexes = list(collection.list_indexes())
        except OperationFailure:
            pass
        else:
            if not any(field in index['key'] for index in indexes):
                try:
                    collection.ensure_index(field, unique=True)
                except DuplicateKeyError:
                    pass

    @property
    def get_users_id(self):
        total_bigv_id = []
        fields = {'usr_id': 1}

        for docs in self.user.find({}, fields):
            bigv_id = docs.get('usr_id')

            if bigv_id:
                total_bigv_id.append(bigv_id)

        return total_bigv_id

    def insert2mongo(self, collection, data):
        try:
            collection.insert(data)
        except Exception:
            pass

    def close(self):
        self.client.close()





