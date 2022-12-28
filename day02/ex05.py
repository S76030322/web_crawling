import requests,re,os
from bs4 import BeautifulSoup

res = requests.get('https://comic.naver.com/webtoon/weekday')
soup = BeautifulSoup(res.text,'html.parser')

web_index = soup.select('.col_inner')
web_thumb = soup.select('.col_inner > ul > li > a')

for i in web_index:
    # print(i.select_one('h4').get('class'))
    weekday = i.select_one('h4').get('class')
    try:
        os.mkdir('C:/Users/ASUS/Desktop/web_crawling/day02/images/'+str(weekday[0]))
    except:
        pass

dic = {}
for i in web_thumb:
    num = i.get('href').split('&')[0].split('=')[1]
    day = i.get('href').split('&')[1].split('=')[1]
    # print(num,day)
    dic[num]=day

for k,v in dic.items():
    res = requests.get(f'https://comic.naver.com/webtoon/list?titleId={k}&weekday={v}')
    soup = BeautifulSoup(res.text,'html.parser')

    title = soup.select_one('.thumb > a > img').get('title')
    title = re.sub('[\/:*?"<>|]',"_",title)
    img = soup.select_one('.thumb > a > img').get('src')
    res = requests.get(img)
    x = img.split('.')[-1]

    # print(type(img))

    try:
        f = open(f"C:/Users/ASUS/Desktop/web_crawling/day02/images/{v}/{title}.{x}","wb")
        f.write(res.content)
    except:
        pass

# https://comic.naver.com/webtoon/list?titleId={}&weekday={}