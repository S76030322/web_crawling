import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/detail?titleId=800506&no=28&weekday=tue")
soup = BeautifulSoup(res.text, "html.parser")

li = soup.select("span.title")
print(li[0].text)
print(soup.select(".wrt_nm")[0].text.strip())
print(soup.select_one(".detail > p").text)
print(soup.select_one("span.genre").text)
print(soup.select_one(".age").text)