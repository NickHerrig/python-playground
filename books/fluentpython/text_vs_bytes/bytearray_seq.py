cafe = bytes('café', encoding='utf_8')
# each byte is a number in range(256)
# No literal syntax for bytearray
for item in cafe:
    print(item)

