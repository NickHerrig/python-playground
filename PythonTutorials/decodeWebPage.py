# Python3

import requests
from bs4 import BeautifulSoup


url = 'https://deltawholesaletire.com/prices/'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html, features="html.parser")


brandList = [head.text for head in soup.find_all(class_='model column')]
priceList = [head.text for head in soup.find_all(class_='price column')]

while 'PRICE/ EA. TIRE' in priceList:
	priceList.remove('PRICE/ EA. TIRE')
priceList.remove('PRICE/ EA. PART')

priceBrandDict = dict(zip(brandList, priceList))
print(priceBrandDict)
