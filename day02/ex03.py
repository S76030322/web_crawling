import requests
from bs4 import BeautifulSoup

# crawling이 막혀있을 경우 우회해서 접근!
res = requests.get('https://www.melon.com')
print(len(res.text)) # 결과 : 0

# what is my user agent >> 내 사용자 에이전트 사용
u_agent = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
res = requests.get('https://www.melon.com',headers=u_agent)
print(len(res.text))