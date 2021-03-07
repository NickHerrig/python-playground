def main():
    needles = {1, 2}
    haystack = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # Intersection
    print(needles & haystack)
    print(needles.intersection(haystack))

    from dis import dis
    # set literals
    print('This is slower!')
    print(dis('set([1, 2, 3])'))
    print('_________________')
    print('This is faster!')
    print(dis('{1, 2, 3}'))

    print(frozenset({1, 2, 3}))

if __name__=="__main__":
    main()

