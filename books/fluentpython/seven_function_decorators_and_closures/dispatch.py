from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<pre>{0}</pre>'.format(content)


def main():
    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize(42))
    print(htmlize('Heimlich & Co.\n- a game'))
    print(htmlize(['alpha', 66, {3, 2, 1}]))


if __name__=="__main__":
    main()

