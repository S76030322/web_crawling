from selenium import webdriver
from selenium.webdriver.common.by import By
import time

a = 'https://edueroom.co.kr/'
driver = webdriver.Chrome('C:/Users/ASUS/Desktop/web_crawling/day03/chromedriver.exe')
driver.get(a)

login = driver.find_element(By.CSS_SELECTOR,".util > li > a")
login.click()

id = driver.find_element(By.CSS_SELECTOR,"#userid_id")
pwd = driver.find_element(By.CSS_SELECTOR,"#passwd_id")
btn = driver.find_element(By.CSS_SELECTOR,".login_btn")

id.send_keys('chsong952001')
pwd.send_keys('Inbc1674!')

time.sleep(5)
btn.click()

user = driver.find_element(By.CSS_SELECTOR,".util")
print(user.text)

time.sleep(10)