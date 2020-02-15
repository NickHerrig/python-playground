import sys
# The equation..
table = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
    }


def hex_to_dec(hexadecimal):
    #TODO


def dec_to_hex(decimal):
    """
    repeatedly divid x by 16, giving a quotient q and a remainder r, such that
    x = q * 16 + r

    EXAMPLE:
    314156 = 19634 . 16 + 12
    19634 = 1227 . 16 + 2 (C)
    1227 = 76 . 16 + 11
    76 = 4 . 16 + 12 (B)
    4 = 0 . 16 + 4 (4)
    
    HEX:
    0x4CB2C
    
    """
    hexadecimal = []
    while True:
        quotient = decimal // 16
        remainder = decimal % 16
    
        if remainder == 0:
            break
    
        if str(remainder) in table.keys():
            hexadecimal.append(table[str(remainder)])
        else:
            hexadecimal.append(str(remainder))
    
        decimal = quotient 

    hexadecimal.reverse()
    return ''.join(hexadecimal)

print(dec_to_hex(int(sys.argv[1])))

#built ins
print(hex(int(sys.argv[1])), 'HEX')
print(bin(int(sys.argv[1])), 'BIN')
print(int(sys.argv[1]), 'INT')



