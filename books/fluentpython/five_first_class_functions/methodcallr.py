from operator import methodcaller


def main():
    s = 'The time has come.'
    upcase = methodcaller('upper')
    print(upcase(s))

    hiphen = methodcaller('replace', ' ', '-')
    print(hiphen(s))

if __name__=="__main__":
    main()

