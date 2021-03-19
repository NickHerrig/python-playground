import unicodedata
import string


def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved_txt = ''.join(c for c in norm_txt
                            if not unicodedata.combining(c))
    return shaved_txt


def main():
    print(shave_marks("Herr Voß: • 1⁄2 cup of ŒtkerTM caffè latte • bowl of açaí."))


if __name__=="__main__":
    main()

