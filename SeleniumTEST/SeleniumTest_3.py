import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")
#time to wait
time.sleep(2)
search = driver.find_element(by=By.NAME,value="q")
search.send_keys("Fluffy Pancakes")
#TIME TO WAIT
time.sleep(5)
#Find Element Finding Button
search_btn = driver.find_element(by=By.XPATH,value="//input[@value='Buscar con Google'][1]")
search_btn.click()
time.sleep(5)
#Navigate back button
driver.back()
time.sleep(2)
#refresh
driver.refresh()
time.sleep(2)
#FORDWARD BUTT
driver.forward()
time.sleep(2)
