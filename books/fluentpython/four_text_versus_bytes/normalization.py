from unicodedata import normalize

def main():
    s1 = 'café'
    s2 = 'cafe\u0301'
    print("length 1: ", len(s1), "length 2: ", len(s2))
    print("length 1: ", len(normalize('NFC', s1)), "length 2: ", len(normalize('NFC', s2)))
    print(s1 == s2)
    print(normalize('NFC', s1) == normalize('NFC', s2))


if __name__=="__main__":
    main()

