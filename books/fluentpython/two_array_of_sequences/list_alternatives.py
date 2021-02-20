def array_demo():
    from array import array
    from random import random
    floats = array('d', (random() for i in range(10**7)))
    print(floats[-1])

    with open('floats.bin', 'wb') as f:
        floats.tofile(f)

    loaded_floats = array('d')
    with open('floats.bin', 'rb') as f:
        loaded_floats.fromfile(f, 10**7)

    print(loaded_floats[-2])
    print(floats==loaded_floats)

if __name__=="__main__":
    array_demo()
