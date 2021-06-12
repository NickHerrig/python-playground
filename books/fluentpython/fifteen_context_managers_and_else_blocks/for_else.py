class Icecream():
    def __init__(self, flavor):
        self.flavor = flavor


my_list = [
    Icecream('chocolate'),
    Icecream('banana'),
    Icecream('vanilla'),
        ]


def main():
    for item in my_list:
        if item.flavor == 'banana':
            break
    else:
        raise ValueError('No banana flavor found!')


if __name__=='__main__':
    main()

