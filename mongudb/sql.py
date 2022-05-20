from pymongo import MongoClient


class Mongo():
    def __init__(self, database: str, url: str):
        self.__database = database
        self.__collection = None
        self.__document = None
        self.__url = url
        self.__query = {}
        self.__projection = {}
        self.__connect()

    def __connect(self):
        self.__con = MongoClient(self.__url)[self.__database]

    def select(self, columns: list):
        self.__projection = {'_id': 0}
        for c in columns:
            self.__projection[c] = 1
        return self

    def from_(self, collection):
        self.__collection = self.__con[collection]
        return self

    def into(self, collection, many=False):
        if many:
            self.__con[collection].insert_many(self.__document)
        else:
            self.__con[collection].insert_one(self.__document)
        return self

    def where(self, field: str, value):
        self.__query[field] = value
        return self

    def and_(self, field: str, value):
        return self.where(field, value)

    def iter(self, one=False, sort=None):
        if one:
            return [self.__collection.find_one(self.__query, self.__projection, sort=sort)]
        else:
            return self.__collection.find(self.__query, self.__projection, sort=sort)

    def show(self, one=False,sort=None):
        for item in self.iter(one, sort):
            print(item)

    def insert(self, object: dict):
        self.__document = object
        return self
