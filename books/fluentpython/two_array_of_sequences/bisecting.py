import bisect

def main():

    haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

    print('haystack ->', ' '.join('%2d' % n for n in haystack))
    ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

    for needle in reversed(needles):
        position = bisect.bisect(haystack, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__=="__main__":
    main()

