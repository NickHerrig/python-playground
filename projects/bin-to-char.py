

def bin_to_char(byte_list):
    """Accepts a list of binary digits, and returns a sentance"""

    num_list = [ int(byte, 2) for byte in byte_list ]
    char_list = [ chr(num) for num in num_list]
    sentance = "".join(char_list)

    return sentance


def main():

    with open("love-note.txt") as f:
        byte_list = f.read().splitlines()

    sentance = bin_to_char(byte_list)

    print(sentance)

if __name__=="__main__":
    main()
