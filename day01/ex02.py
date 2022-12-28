import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.com")
print("res :",res)
print("text ===>",res.text)

soup = BeautifulSoup(res.text,'html.parser')
print('select one')
print(soup.select_one('.nav_item'))

print('select')
print(soup.select('.nav_item'))

print('=== for ===')
for i in soup.select('.nav_item'):
    print(i.select('a'))

