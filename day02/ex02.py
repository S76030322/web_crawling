import requests
from bs4 import BeautifulSoup

res = requests.get('https://comic.naver.com/webtoon/weekday')
soup = BeautifulSoup(res.text,'html.parser')

print(soup.select(".view_type > ul > li > a"))
print(soup.select_one(".view_type").text.split())

print('=='*30)

# print(soup.select('#container'))
# print(soup.select('.col > .col_inner > h4 '))
# print(soup.select('.col > .col_inner > ul'))
# print(soup.select('.col > .col_inner > ul > li > .thumb > a'))

# class 의 값이 href값의 weekday={}에 삽입 되어야 요일별 웹툰을 출력할 수 있음

# web_day = soup.select('.col > .col_inner > h4 ')
web_index = soup.select('.col > .col_inner > ul > li > .thumb > a')
web_name = soup.select('.col > .col_inner > ul > li > .thumb > a > img')


# for i in web_day:
#     print(i.get('class'))

dic = {}
for i in web_index:
    title = i.select_one('img').get('title')
    # print(title.get('title'))
    # # print(i.get('href').split('&'))
    num = i.get('href').split('&')[0].split('=')[1]
    day = i.get('href').split('&')[1].split('=')[1]

    dic[num] = day

    # print(f'제목: {title}\n번호: {num}, 요일: {day}\n')

for k,v in dic.items():

    res = requests.get(f'https://comic.naver.com/webtoon/list?titleId={k}&weekday={v}')
    soup = BeautifulSoup(res.text,'html.parser')

    web_index = soup.select('.comicinfo > .detail')

    writer = []
    for i in web_index:
        title = i.select_one('h2 > .title').text
        wrt_nm = i.select_one('h2 > .wrt_nm').text.split()
        for j in range(len(wrt_nm)):
            if wrt_nm[j] == '/':
                continue
            writer.append(wrt_nm[j])
        genre = i.select_one('p > .genre').text.split()[1]
        age = i.select_one('p > .age').text
        detail = i.select_one('p').text
        print(f'\n제목: {title}\n작가: {writer}\n장르: {genre}\n연령: {age}\n설명: {detail}\n')
        print('====='*33)