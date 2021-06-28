def chain(*iterables):
    for it in iterables:
        yield from it


def main():
    '''Description of the function'''
    my_list = ['hello', 'world', 'nick', 'bye']
    new_list = list(chain(my_list, range(10)))
    print(new_list)

if __name__ == '__main__':
    main()

