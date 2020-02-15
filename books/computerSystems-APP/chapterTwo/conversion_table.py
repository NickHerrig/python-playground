from collections import namedtuple

number = namedtuple('number', 'hexadecimal binary')

number_conversion_table = { 
    '0': number(0x0, 0b0000),
    '1': number(0x1, 0b0001),
    '2': number(0x2, 0b0010),
    '3': number(0x3, 0b0011),
    '4': number(0x4, 0b0100),
    '5': number(0x5, 0b0101),
    '6': number(0x6, 0b0110),
    '7': number(0x7, 0b0111),
    '8': number(0x8, 0b1000),
    '9': number(0x9, 0b1001),
    '10': number(0xa, 0b1010),
    '11': number(0xb, 0b1011),
    '12': number(0xc, 0b1100),
    '13': number(0xd, 0b1101),
    '14': number(0xe, 0b1110),
    '15': number(0xf, 0b1111),
}

