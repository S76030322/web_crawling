import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/index")
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select_one('.tab_gr').text.split())
print(soup.select_one('.sortby').text.split())

print(soup.select_one('.genreRecomImg2 > a').get('href'))
a = soup.select_one(".genreRecomImg2 > a").get("href")
print(a.split("="))
a_split = a.split("=")
print(a_split[-1])

print('='*50)
href_list = soup.select('.genreRecomImg2 > a')
title_list = soup.select('.genreRecomImg2 > a > img')

for i in range(len(href_list)):
    href = href_list[i].get('href')
    title = title_list[i].get('title')
    print(title,':',href.split('=')[-1])
