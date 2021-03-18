from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def case_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


def main():

    print(nfc_equal('hello', 'hello'))
    print(nfc_equal('hello', 'hEllO'))
    print(case_equal('hello', 'hEllO'))

if __name__=="__main__":
    main()

