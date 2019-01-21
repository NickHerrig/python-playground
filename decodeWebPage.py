# Python3

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/section/business'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
