import serial

s = serial.Serial('/dev/cu.usbserial-DN04SV8H',
                  baudrate=38400,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS)

