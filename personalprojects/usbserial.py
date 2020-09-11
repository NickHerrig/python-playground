import serial

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

"""

# ID will come from interface client
# functioncode will come from interface client
# data will come from interface client (TODO: what type of data can be sent for what commands? Speed? Position? Units?)
# packet length will have to be calculated (Varies between 4 bytes and 7 bytes, data causes the variablility 1-4 bytes).
# checksum is calculated where Sum is sum of bytes:  (Sum % 128)| 0b10000000
