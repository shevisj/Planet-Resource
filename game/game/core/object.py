from hashlib import sha256
from jsonpickle import encode, decode
from jsonpickle.ext import numpy as jsonpickle_numpy
jsonpickle_numpy.register_handlers()

class CoreObject(object):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialize(obj):
        return decode(obj)

    def serialize(self):
        return encode(self)

    def hash(self):
        return sha256(self.serialize()).hexdigest()
