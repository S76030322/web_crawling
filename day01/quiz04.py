import requests
from bs4 import BeautifulSoup

while True:
    search = input('news search : ')
    res = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={search}")

    soup = BeautifulSoup(res.text, "html.parser")
    #print(soup.select(".news_area > a"))

    print("--- 뉴스 제목 ---")
    for i in soup.select(".news_area > a"):
        print(i.text)