from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests,time

driver = webdriver.Chrome()
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EA%B3%A0%EC%96%91%EC%9D%B4")

# res = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EA%B3%A0%EC%96%91%EC%9D%B4")
# soup = BeautifulSoup(res.text,"html.parser")

time.sleep(3)

soup = BeautifulSoup(driver.page_source,"html.parser")
img = soup.select_one(".thumb > .link_thumb > img") # page가 load될때까지 시간이 걸리므로 time.sleep()기능을 사용하자. >> 사용X None처리 된다.

print(img)
