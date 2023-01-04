from selenium import webdriver
from selenium.webdriver.common.by import By # By >> 선택자

driver = webdriver.Chrome("C:/Users/ASUS/Desktop/web_crawling/day03/chromedriver.exe")
driver.get("https://www.naver.com")

search = driver.find_element(By.CSS_SELECTOR,"#query")
search.send_keys("오늘의 날씨")

search_btn = driver.find_element(By.CSS_SELECTOR,"#search_btn")
search_btn.click()

input()

'''
    요소지정
     - find_element : 요소하나
     - find_elements : 여러개 요소

    행동
     - .click() : 클릭
     - .send_keys() : 값을 넣어줌
     - .text : 텍스트 부분 추출
     - .get_attribute(속성명) : 속성값 추출
    
    By
     - By.ID : 태그의 id값 추출
     - By.Name : name값 추출
     - By.XPATH : 경로
     - By.LINK_TEXT : 링크 텍스트
     - By.CLASS_NAME : 클래스 명
     - By.CSS_SELECTOR : CSS선택자 추출
'''

# test