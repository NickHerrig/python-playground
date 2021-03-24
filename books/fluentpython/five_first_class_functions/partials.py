import unicodedata, functools
from func_params import tag

def main():
    nfc = functools.partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'

    print(s1, s2)
    print(s1 == s2)
    print(nfc(s1) == nfc(s2))

    picture = functools.partial(tag, 'img', cls='pic-frame')
    print(picture(src='testing.jpeg'))
    print(picture.func)
    print(picture.args)
    print(picture.keywords)


if __name__=="__main__":
    main()

