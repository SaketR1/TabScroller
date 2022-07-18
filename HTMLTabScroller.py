#Selenium webdriver is needed in order to locate the tabs by their HTML code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s) #setting up webdriver

import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://192.168.5.87:8000") #change this to the dashboard's URL page
driver.maximize_window()

program_should_run = True

try:
    while(program_should_run):
        
        #dashboardTabs is a list of all of the tabs on the webpage
        dashboardTabs = driver.find_elements(By.CLASS_NAME, "nav-item")
        
        for i in dashboardTabs:
            
            """
            If the mouse is in the very top left corner of the screen,
            the program will automatically stop. Use this if the program 
            for some reason continues to click the screen
            even if you stopped the program.
            """
            if ((pyautogui.position().x == 0) and (pyautogui.position().y == 0)):
                program_should_run = False
                break
            
            """
            For every tab on the webpage, the program will click it.
            Then, after a second, it will scroll to the bottom so the entire webpage
            is loaded. Then it will sleep for a certain amount of time.
            
            The program should automatically adjust if a new tab is added to the
            webpage. However, it might take a while since the program needs to reach
            the end of the current number of tabs.
            """
            i.click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4) #Adjust how long the program stops for in seconds
except:
    print("Could not find")

"""
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:8000/")
"""
