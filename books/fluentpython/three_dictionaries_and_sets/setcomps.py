def main():

    from unicodedata import name
    signs = { chr(i) for i in range(0, 256) if 'SIGN' in name(chr(i), '')}
    print(signs)
    lowerletter = { chr(i) for i in range(0, 256) if 'SMALL LETTER' in name(chr(i), '')}
    print(lowerletter)


if __name__=="__main__":
    main()

