from pprint import pprint

from bs4 import BeautifulSoup
import requests

url = 'https://ohospitality.com/events/'
r = requests.get(url)

html = BeautifulSoup(r.content, 'html.parser')
h3 = html.find_all('h3')

for event in h3:
    print(event.string)
