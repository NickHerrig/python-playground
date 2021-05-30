"""
    >>> s = Sentence("hello my name is nick")
    >>> s[0]
    'hello'
    >>> len(s)
    5
    >>> s
    Sentence('hello my name is nick')
    >>> " ".join((word for word in s))
    'hello my name is nick'


"""

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
