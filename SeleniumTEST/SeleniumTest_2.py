import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")
#time to wait
time.sleep(2)
#Get the url
title = driver.title
print("the title is -->", title)
assert title == "Googlee", f"Title doesn't matched the expected is Googlee but is actual is{title}"
print("Test Finished")