import pyuca


def main():
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

    coll = pyuca.Collator()
    sorted_fruits = sorted(fruits, key=coll.sort_key)

    wrong_sorted_fruits = sorted(fruits)

    print("Incorrectly sorted fruits...")
    print(wrong_sorted_fruits)
    print("Correctly sorted fruits!")
    print(sorted_fruits)


if __name__=="__main__":
    main()

