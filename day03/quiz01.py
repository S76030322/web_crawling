from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time,os,re,requests

# 정보받기
img_ch = input('이미지 검색: ')

# 페이지 연결
browser = webdriver.Chrome()
browser.get('https://www.naver.com')

time.sleep(1)

# 받은 정보 전달
br_in = browser.find_element(By.CSS_SELECTOR,".input_text")
br_in.send_keys(img_ch)

# 버튼 >> 페이지 이동
br_btn = browser.find_element(By.CSS_SELECTOR,".btn_submit")
br_btn.click()

# 페이지 이동 후 경로 선택
br_path = browser.find_elements(By.CSS_SELECTOR,".base > .menu")

for i in br_path:
    # print(i.text)
    if i.text == "이미지":
        i.click()
        break

# 폴더 생성
try:
    os.mkdir('C:/Users/ASUS/Desktop/web_crawling/day03/images/'+str(img_ch))
except:
    pass

# 정보 추출(이미지)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,"html.parser")
img = soup.select(".thumb > .link_thumb > img")

for i in img:
    # print(i,"\n")

    x = i.get("src")
    
    # https로 시작하는 값만 추출 >> 관리자가 새로운 값을 만들시 오류 발생을 미연에 방지
    try:
        if x.split(":")[0] == "data":
            x = i.get("data-lazy-src")
    except:
        pass
    
    # 이미지 확장자, 이름, 정규표현식
    img_type = x.split("&")[0].split(".")[-1]
    img_name = i.get("alt")
    img_name = re.sub('[\/:*?"<>|]',"_",img_name)
    # print(img_type)
    # print(x,"\n")

    # 이미지 경로 요청
    res = requests.get(x)

    try:
        f = open(f"C:/Users/ASUS/Desktop/web_crawling/day03/images/{img_ch}/{img_name}.{img_type}","wb")
        f.write(res.content)
    except:
        pass

time.sleep(5)


# [ 네이버 ]
# "https"로 가져오는 것 data-lazy-src, src