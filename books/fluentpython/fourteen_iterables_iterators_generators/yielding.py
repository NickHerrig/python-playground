def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def new_chain(*iterables):
    for i in iterables:
        yield from i

def main():
    s = 'ABC'
    t = tuple(range(5))
    my_list = list(chain(s, t))
    print(my_list)

    my_list = list(new_chain(s, t))
    print(my_list)


if __name__=="__main__":
    main()

