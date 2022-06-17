from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)

import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://192.168.5.87:8000")
driver.maximize_window()

program_should_run = True

try:
    while(program_should_run):
        dashboardTabs = driver.find_elements(By.CLASS_NAME, "nav-item")
        for i in dashboardTabs:
            if ((pyautogui.position().x == 0) and (pyautogui.position().y == 0)):
                program_should_run = False
                break
            i.click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
except:
    print("Could not find")

"""
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:8000/")
"""
