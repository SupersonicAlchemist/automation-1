import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.current_url)
print(driver.title)
driver.maximize_window()
driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys('ber')
time.sleep(2)
berryclicks = driver.find_elements(By.XPATH, "//div/div/div[@class='product-action']")
for berryclick in berryclicks:
    berryclick.click()
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
time.sleep(10)
 
