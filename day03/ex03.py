from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Users/ASUS/Desktop/web_crawling/day03/chromedriver.exe')
driver.get('https://www.naver.com')

nav = driver.find_elements(By.CSS_SELECTOR, "#gnb > .gnb_inner > .group_nav > ul > li ")

for i in nav:
    x = i.find_element(By.TAG_NAME,"a")
    # print(x.text,":",x.get_attribute("href"))

    if x.text == "웹툰":
        x.click()
        break

time.sleep(3)

menu = driver.find_elements(By.CSS_SELECTOR,".menu > li")

for i in menu:
    x = i.find_element(By.TAG_NAME,"a")
    # print(x.get_attribute("href"))

    if x.text == "웹툰":
        x.click()
        break

time.sleep(3)
