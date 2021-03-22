
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def main():
    print(tag('br'))
    print(tag('p', 'hello world'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', cls='greeting'))

    my_attrs = {'name': 'p', 'content': 'hello'}
    print(tag(**my_attrs))


if __name__=="__main__":
    main()

