import requests,re,os
from bs4 import BeautifulSoup

# 확장자에 맞춰서 생성하기
res = requests.get('https://shared-comic.pstatic.net/thumb/webtoon/602916/thumbnail/thumbnail_IMAG04_a0f09d89-b921-4a30-ba15-e2984c2dda34.jpg')
soup = BeautifulSoup(res.text,'html.parser')

f = open("C:/Users/ASUS/Desktop/web_crawling/day02/images/test.jpg","wb")
f.write(res.content)

# import re >> python에서 정규 표현식을 사용할때 가져온다

title = "010-15?66##1212"
title = re.sub('[\/:*?"<>|#-]',"",title)
print(title)

for i in range(10):
    try: 
        # os.mkdir('C:/Users/ASUS/Desktop/web_crawling/day02/images/'+str(i+1)+"폴더")
        os.rmdir('C:/Users/ASUS/Desktop/web_crawling/day02/images/'+str(i)+"폴더")
    except:
        pass