def main():

    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts  = [(color, size) for color in colors
                              for size in sizes]

    from pprint import pprint
    pprint(tshirts)


if __name__=="__main__":
    main()

