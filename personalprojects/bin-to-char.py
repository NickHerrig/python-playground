
def main():

    with open("love-note.txt") as f:
        byte_list = f.read().splitlines()

    num_list = [ int(byte, 2) for byte in byte_list ]
    char_list = [ chr(num) for num in num_list ]
    sentance = "".join(char_list)

    print(sentance)

if __name__=="__main__":
    main()
