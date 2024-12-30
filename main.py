from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import json
import time

login_info = json.load(open('login_info.json','r'))

service = Service(executable_path='C:\Denis\Programs\Duckies\chromedriver-win64\chromedriver.exe') 
driver = webdriver.Chrome(service=service)

driver.get('https://parents.sbschools.org/genesis/sis/view?gohome=true')

username_input = driver.find_element(By.ID, 'j_username')
username_input.send_keys(login_info['username'])

password_input = driver.find_element(By.ID, 'j_password')
password_input.send_keys(login_info['password'] + Keys.ENTER)


time.sleep(10)
driver.quit()