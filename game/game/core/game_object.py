from uuid import uuid4
from hashlib import sha256
from jsonpickle import encode, decode
from jsonpickle.ext import numpy as jsonpickle_numpy
jsonpickle_numpy.register_handlers()

class GameObject(object):
    def __init__(self):
        self.uuid = uuid4().hex
        super().__init__()

    @classmethod
    def deserialize(cls, obj):
        return decode(obj)

    def serialize(self):
        return encode(self)

    def hash(self):
        self.hash = sha256(str(self.serialize()).encode('utf-8')).hexdigest()
        return self.hash

    def __str__(self):
        return self.__class__.__name__
