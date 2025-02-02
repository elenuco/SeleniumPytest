import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")
#time to wait
time.sleep(2)
#Maximize window
driver.maximize_window()
#Time
time.sleep(5)
#Minimize window
driver.minimize_window()
time.sleep(5)
#close
driver.close()