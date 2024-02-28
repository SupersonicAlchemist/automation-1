import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
print(driver.current_url)
print(driver.title)
driver.maximize_window()
radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radios))
for radio in radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        break

time.sleep(5)
