import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
moblists = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for moblist in moblists:
    prodname = moblist.find_element(By.XPATH, "div/h4").text
    print(prodname)
    if prodname == "Blackberry":
        moblist.find_element(By.XPATH, "div/button").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "active").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
time.sleep(7)
driver.find_element(By.XPATH, "//a[text()='India']").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
ValidationText = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in ValidationText



