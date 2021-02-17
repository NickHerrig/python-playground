def main():
    print("Slicing steps...")
    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    print("Slicing objects and displaying skus!")

    invoice = """
    0.....6....................
    1909 Pimoroni PiBrella
    1489 6mm Tactile Switch x20
    1510 Panavise Jr. - PV-201
    1601 PiTFT Mini Kit 320x240
    """

    SKU = slice(4, 8)
    line_items = invoice.split('\n')[2:]
    for item in line_items:
        print(item[SKU])

    print("mutability and slicing...")
    l = list(range(15))
    print(l)
    del(l[3:6])
    print(l)
    l[5:9] = [45]
    print(l)


if __name__=="__main__":
    main()

