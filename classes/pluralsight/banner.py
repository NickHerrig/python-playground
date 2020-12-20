
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

def main():
    x = input("please add banner: ")
    banner(x)

if __name__ == '__main__':
    main()
