import time
from selenium import webdriver
print("Start")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)
print("done")