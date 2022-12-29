from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,pyperclip

driver = webdriver.Chrome('C:/Users/ASUS/Desktop/web_crawling/day03/chromedriver.exe')
driver.get('https://www.naver.com')

n_click = driver.find_element(By.CSS_SELECTOR,'.link_login')
n_click.click()

time.sleep(2)

user_id = "userID"
user_pw = "userPWD"

# id 복사 붙여넣기
n_id = driver.find_element(By.CSS_SELECTOR,'#id')
pyperclip.copy(user_id)
n_id.send_keys(Keys.CONTROL,'v')
time.sleep(1)

# pw 복사 붙여넣기
n_pw = driver.find_element(By.CSS_SELECTOR,'#pw')
pyperclip.copy(user_pw)
n_pw.send_keys(Keys.CONTROL,'v')
time.sleep(1)

# 버튼 클릭
btn = driver.find_element(By.CSS_SELECTOR,'.btn_login')
btn.click()
time.sleep(5)