from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/ASUS/Desktop/web_crawling/day03/chromedriver.exe')
driver.get('https://www.daum.net')

# nav = driver.find_element(By.CSS_SELECTOR, ".list_mainsvc > li")
# print(nav.text)
# nav.click()
nav = driver.find_elements(By.CSS_SELECTOR, ".list_mainsvc > li")
# print(nav)

for i in nav:
    # print(i.find_element(By.TAG_NAME,"a"))

    k = i.find_element(By.TAG_NAME, "a")
    print(k.text,":",k.get_attribute("href"))

input()