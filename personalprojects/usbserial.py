from math import log

#import serial


#s = serial.Serial(os.getenv('USB_PORT'),
#                  baudrate=38400,
#                  parity=serial.PARITY_NONE,
#                  stopbits=serial.STOPBITS_ONE,
#                  bytesize=serial.EIGHTBITS)

"""
Drive is little endian.

ID = One byte (Start byte)
packetLenght + functioncode = One byte
data = One - Four bytes
checksum = One byte

Packet = B0 B1 B2 B3 B4 B5 B6 B7

"""
def count_bytes(data):
    """Return number of bytes of data 1-4"""
    #TODO: should data=0 or less reach here?
    return int(log(data, 256)) + 1

def main():
    packet_length = 3 + count_bytes()
    print(packet_length)

if __name__=='__main__':
    main()


# ID will come from interface client
# functioncode will come from interface client
# data will come from interface client (TODO: what type of data can be sent for what commands? Speed? Position? Units?)
# packet length will have to be calculated (Varies between 4 bytes and 7 bytes, data causes the variablility 1-4 bytes).
# checksum is calculated where Sum is sum of bytes:  (Sum % 128)| 0b10000000
