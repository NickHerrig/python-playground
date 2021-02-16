def main():

    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts  = ( (color, size) for color in colors
                              for size in sizes)


    print(tshirts)

    for shirt in tshirts:
        print(shirt)



if __name__=="__main__":
    main()

