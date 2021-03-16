import sys, locale

def main():
    expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

    my_file = open('dummy', 'w')

    for exp in expressions.split():
        value = eval(exp)
        print(exp.rjust(30), '->', repr(value))


if __name__=="__main__":
    main()

