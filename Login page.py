from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

service_Obj = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj, options=options)
driver.get("https://awn-sa.com/login")
# driver.find_element(By.CSS_SELECTOR, "li:nth-child(4)").click()
driver.find_element(By.ID, "email").send_keys("superadmin@awn.com")
driver.find_element(By.ID, "password").send_keys("root@123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
driver.close()
