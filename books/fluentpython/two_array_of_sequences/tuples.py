def main():
    lax_coordinates = ( 123.1231, -118.4 )

    # tuple unpacking
    latitude, longitude = lax_coordinates

    print(latitude)

    quotient, remainder = divmod(20,8)
    print(quotient)

    import os
    _, filename = os.path.split('/home/nick/.ssh/idrs.pub')
    print(filename)

    a, b, *rest = range(10)
    print(rest)

    a, *middle, b = range(10)
    print(a, middle, b)



if __name__=="__main__":
    main()

