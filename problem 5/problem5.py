import argparse
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_name',
                    default='C:/Users/test/OneDrive/Pulpit/studia/STOPIEŃ 2/python wZN/problem 5/wiadomosci.json',
                    required=False)
args = parser.parse_args()
nazwa = args.file_name

options = Options()
options.add_argument('--disable-notifications')

service = Service("C:/Users/test/OneDrive/Pulpit/studia/STOPIEŃ 2/python wZN/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://wiadomosci.onet.pl/')
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, '#rasp_cmp > div > div.cmp-intro_options > button.cmp-button_button.cmp-intro_acceptAll')
time.sleep(2)
button.click()
time.sleep(2)

wall = driver.find_element(By.CSS_SELECTOR, '#doc > div.pageContent.pageWrapper > section > div')
# post = wall.find_elements(By.CLASS_NAME, 'mediumNewsBox')
posty = []
for i in range(2):
    time.sleep(1)
    post = wall.find_elements(By.CLASS_NAME, 'mediumNewsBox')

    for j in post:
        tresc = j.find_element(By.CLASS_NAME, 'title').text
        posty.append((tresc.strip()))
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

with open(nazwa, 'w') as f:
    json.dump(posty, f, ensure_ascii=False)

time.sleep(5)
driver.close()