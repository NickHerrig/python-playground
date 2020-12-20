import requests
import re
from pprint import pprint

print("""


8888888b. Y88b   d88P      888b     d888        d8888  .d8888b.  
888   Y88b Y88b d88P       8888b   d8888       d88888 d88P  Y88b 
888    888  Y88o88P        88888b.d88888      d88P888 888    888 
888   d88P   Y888P         888Y88888P888     d88P 888 888        
8888888P"     888          888 Y888P 888    d88P  888 888        
888           888          888  Y8P  888   d88P   888 888    888 
888           888          888   "   888  d8888888888 Y88b  d88P 
888           888          888       888 d88P     888  "Y8888P"  



                                   |\ /| /|_/|
                                 |\||-|\||-/|/|
                                  \\|\|//||///
                 _..----.._       |\/\||//||||
               .'     o    '.     |||\\|/\\ ||
              /   o       o  \    | './\_/.' |
             |o        o     o|   |          |
             /'-.._o     __.-'\   |          |
             \      `````     /   |          |
             |``--........--'`|    '.______.'
              \              /
               `'----------'`
""")


while True:
    
    macaddress = input('MAC Address: ')
    check = re.match('^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$',macaddress)
    if check:

        vendor = 'https://macvendors.co/api/vendorname/'+ str(macaddress)
        
        vendor_response = requests.get(vendor)
        if vendor_response.status_code != 200:
            raise ApiError('GET MAC Failed {}'.format(vendor_response.status_code))
        
        print('_____________________\n')
        pprint(vendor_response.text)

    else:
        print("Please enter a valid MAC Address")
