from collections import UserDict

"""
ezdict or Easy Dictionary, implements lookups with a string, regarless of quotes or not. It is utilized mostly to not "trip-up" stupents using a dictionary for a learning experiment. 

From Fluent Python orginally, and the Ping.io project. 
"""

class EzDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem(self, key, item):
        self.data[str(key)] = item


