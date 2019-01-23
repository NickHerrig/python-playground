# Python3
# Decodes a web page and prints the full text of an article

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html, features="html.parser")

for entry in soup.find_all(class_='content-section'):
	print(entry.text)
