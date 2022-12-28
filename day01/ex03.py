import requests
from bs4 import BeautifulSoup
from ex01 import getHtml

st = getHtml()
print(st)

soup = BeautifulSoup(st,'html.parser')
print(soup.select_one("#care1").get('class'))
print(soup.select_one("#care1").get('id'))
print('=='*40)
print(soup.select_one("#care2").get('id'))
print(soup.select_one("#care3").get('class'))
print(soup.select_one("a").get('href'))