import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/detail?titleId=800506&no=28&weekday=tue")
soup = BeautifulSoup(res.text, "html.parser")

print('웹툰별점')
print(soup.select_one("#topPointTotalNumber > strong"))

print('참여인원')
print(soup.select_one(".pointTotalPerson > em"))

print('웹툰 .detail')
print(soup.select(".detail"))

print('웹툰 .detail의 h2')
for i in soup.select('.detail'):
    print(i.select('h2'))

print('웹툰 .detail의 p')
for i in soup.select('.detail'):
    print(i.select('p'))

print('웹툰 .detail의 ul')
for i in soup.select('.detail'):
    print(i.select('ul'))
