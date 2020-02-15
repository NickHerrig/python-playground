"""
ezdict or Easy Dictionary, implements lookups with a string, regarless of quotes or not. It is utilized mostly to not "trip-up" stupents using a dictionary for a learning experiment. 

From Fluent Python orginally, and the Ping.io project. 
"""

class EzDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __get__(self, key, default=None):
        try:
            return self[key]
        except KeyError:
             return default 

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

