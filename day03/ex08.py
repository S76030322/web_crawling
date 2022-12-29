from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=img&tbm=isch&ved=2ahUKEwim76POoJ78AhUITpQKHdeXB7AQ2-cCegQIABAA&oq=img&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6CAgAELEDEIMBOgQIABADOgsIABCABBCxAxCDAToHCCMQ6gIQJ1DGyQJY7rsEYOe-BGgFcAB4AIABoQGIAcIHkgEDNy4zmAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=BDutY6bdHIic0QTXr56ACw&bih=916&biw=1707")

time.sleep(1)

# height = 0
# while True:
#     driver.execute_script(f"window.scrollTo(0,{height});")
#     time.sleep(1)
#     height += 100

before_height = 0
while True:
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0,{new_height});")
    
    if before_height == new_height:
        break
    before_height = new_height

    print(before_height)    
    time.sleep(0.5)

print(new_height)