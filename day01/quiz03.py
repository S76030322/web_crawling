import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/detail?titleId=800506&no=30")
soup = BeautifulSoup(res.text, "html.parser")

total = int(soup.select_one('span.total').text)
print(total)

start = total-2

for i in range(start,total+1,1):
    res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=800506&no={i}")
    soup = BeautifulSoup(res.text, "html.parser")
    print('페이지 번호 : ',i)
    print('평점 : ',soup.select_one('#topPointTotalNumber > strong').text)
    print('참여수 : ',soup.select_one('.pointTotalPerson > em').text)
    print('등록일 : ',soup.select_one('dd.date').text)
    print()