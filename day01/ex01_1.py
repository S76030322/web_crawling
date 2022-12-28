from ex01 import getHtml
from bs4 import BeautifulSoup

st = getHtml()
# print(st)

soup = BeautifulSoup(st,'html.parser')
string = soup.select_one("div")
print(string)

print('='*40)
string = soup.select("div")
print(string)

print('='*40)
print(soup.select('#care1'))    # '#'은 id
print(soup.select('.lab2'))     # '.'은 class
print(soup.select('div>span'))  # div태그 안에 있는 span태그
print(soup.select('html>body>#care3>span')) # html > body > id=care3 > span