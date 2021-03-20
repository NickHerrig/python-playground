def reverse(word):
    return word[::-1]


def main():

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=reverse))

    #Anonymous Function w/ lambda rather than higher order pass through
    print(sorted(fruits, key=lambda word: word[::-1]))

if __name__=="__main__":
    main()

