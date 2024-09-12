from _pydatetime import time
import time
from asyncio import timeout_at
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))
# Now, wait for the button to be clickable and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#flush-collapseOne']")))
button.click()
time.sleep(5)
driver.find_element(By.ID, "settings").click()
driver.find_element(By.CSS_SELECTOR,"a[href='https://awn-sa.com/settings/faq']").click()
zahid_bhai = driver.find_elements(By.CSS_SELECTOR,".sidebar-nav")
print(zahid_bhai)
time.sleep(10)
# driver.close()