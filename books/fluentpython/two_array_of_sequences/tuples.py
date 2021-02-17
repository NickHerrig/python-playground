def as_records():
    print("Tuples can be used as records!")
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

    from collections import namedtuple

    Pump = namedtuple('Pump', 'ip name')
    a = Pump('127.0.0.1', 'microgreen row one')
    b = Pump('192.168.0.34', 'tomatoes pump')

    print(a._asdict())
    print(a._fields)

    print("The pump ips: ", a.ip, b.ip)


if __name__=="__main__":
    as_records()

