from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time,os,re,base64,requests

# 찾고자 하는 검색어 입력
u_input = input('검색: ')

# google 접속
browser = webdriver.Chrome()
browser.get(f"https://www.google.com/search?q={u_input}")

# 웹페이지 이동 ('이미지')
br_me = browser.find_elements(By.CSS_SELECTOR,".hdtb-mitem > a")

for i in br_me:
    # print(i.text) # 리스트 확인용

    if i.text == "이미지":
        i.click()
        break

# 폴더 생성
try:
    os.mkdir('C:/Users/ASUS/Desktop/web_crawling/day03/images/'+str(u_input))
except:
    pass


# 웹페이지 횡 스크롤 움직이기 위해 설정
before_height = 0
while True:
    
    # 이미지 추출 >> BeautifulSoup사용시 select()의 값 꼭 확인해 볼 것! 
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    br_img = soup.select('.islrc > .isv-r > .wXeWr > div > img')

    # 확인용
    # br_img = soup.select_one('.islrc > .isv-r > .wXeWr > div > img')
    # print(br_img.get('src'))
    # print(br_img.get('data-src'))
    # print(type(br_img.get('src')))
    # print(type(br_img.get('data-src')))
    for i in br_img:
    # print(i) # 리스트 확인용

    # 확인 결과 
    # 방식 : src, data-src 2개 혼용
    # src >> "data"형식, "http"형식 혼용

    # 구글에서 새로운 형식 도입시 에러가 발생 할 수 있으므로 try:except으로 처리
        img_path = i.get('src')
        
        if type(img_path) != str:
            img_path = i.get('data-src')
        
        # 이미지 이름 추출 및 정규표현식
        img_name = i.get('alt')
        img_name = re.sub('[\/:*?"<>|]',"_",img_name)  
        img_type = img_path.split(":")[0]

        # print(img_path)
        # print(img_type)

        # 구글에서 새로운 형식 도입시 에러가 발생 할 수 있으므로 else문 추가
        if img_type == "data": # data형식은 base64로 처리
            print(1) # 확인용
            # 같은 파일 생성시 오류 발생 해결을 위해 try:except문 사용
            try:
                x = img_path.split(",")[1]
                f = open(f"C:/Users/ASUS/Desktop/web_crawling/day03/images/{u_input}/{img_name}.jpeg","wb")
                img = base64.b64decode(f"{x}")
                f.write(img)
                f.close()
            except:
                pass

        elif img_type == "https": # https형식은 requests로 처리
            print(2) # 확인용
            # 같은 파일 생성시 오류 발생 해결을 위해 try:except문 사용
            try:
                res = requests.get(img_path)
                f = open(f"C:/Users/ASUS/Desktop/web_crawling/day03/images/{u_input}/{img_name}.jpeg","wb")
                f.write(res.content)
                f.close()
            except:
                pass

        else:
            continue

    new_height = browser.execute_script("return document.documentElement.scrollHeight")
    browser.execute_script(f"window.scrollTo(0,{new_height});")
    
    # 멈춰!
    if before_height == new_height:
        break
    before_height = new_height

    # print(before_height) # 확인용
    



'''for i in br_img:
    # print(i) # 리스트 확인용

    # 확인 결과 
    # 방식 : src, data-src 2개 혼용
    # src >> "data"형식, "http"형식 혼용

    # 구글에서 새로운 형식 도입시 에러가 발생 할 수 있으므로 try:except으로 처리
    img_path = i.get('src')
    
    if type(img_path) != str:
        img_path = i.get('data-src')
    
    # 이미지 이름 추출 및 정규표현식
    img_name = i.get('alt')
    img_name = re.sub('[\/:*?"<>|]',"_",img_name)  
    img_type = img_path.split(":")[0]

    # print(img_path)
    # print(img_type)

    # 구글에서 새로운 형식 도입시 에러가 발생 할 수 있으므로 else문 추가
    if img_type == "data": # data형식은 base64로 처리
        print(1) # 확인용
        # 같은 파일 생성시 오류 발생 해결을 위해 try:except문 사용
        try:
            x = img_path.split(",")[1]
            f = open(f"C:/Users/ASUS/Desktop/web_crawling/day03/images/{u_input}/{img_name}.jpeg","wb")
            img = base64.b64decode(f"{x}")
            f.write(img)
            f.close()
        except:
            pass

    elif img_type == "https": # https형식은 requests로 처리
        print(2) # 확인용
        # 같은 파일 생성시 오류 발생 해결을 위해 try:except문 사용
        try:
            res = requests.get(img_path)
            f = open(f"C:/Users/ASUS/Desktop/web_crawling/day03/images/{u_input}/{img_name}.jpeg","wb")
            f.write(res.content)
            f.close()
        except:
            pass

    else:
        continue
'''
time.sleep(2)
