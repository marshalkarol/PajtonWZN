from selenium import webdriver
import time
import argparse
from ast import arg

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service


parser = argparse.ArgumentParser()
parser.add_argument('-f','--file_name', default = 'live06 - problem 5/problem 5/cdptwitter.json', required = False)
args = parser.parse_args()
nazwa = args.file_name


options = Options()
options.add_argument('--disable-notifications')

service = Service("C:/Users/karol/Desktop/studia/1 stopień/chrome selenium webdriver/chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)
driver.get('https://twitter.com/cdprojektred')
time.sleep(2)


#layers > div > div:nth-child(2) > div > div > div > div.css-1dbjc4n.r-eqz5dr.r-1joea0r.r-1r5su4o > div:nth-child(1) > div    ale nie działało (jako selector)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/div[2]/div[1]')
time.sleep(2)
button.click()
time.sleep(2)



for i in range(4):
    time.sleep(1)
    #cards = driver.find_elements(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article')    
    username = driver.find_element(By.XPATH, '//*[@id="id__66cbm90xhds"]/div[1]/div/a/div/div[1]/span/span')
    print(username)

    # for tekst in cards:
        # username = tekst.find_element(By.CSS_SELECTOR, 'id__zcoxsz5iyro > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wbh5a2.r-dnmrzs > div > a > div > div.css-901oao.r-1awozwy.r-1nao33i.r-6koalj.r-37j5jr.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0 > span > span').text
        # message = tekst.find_element(By.ID, 'id__ou70muluuoe').text
        # print(username)
        # print(message)
    print()
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

time.sleep(5)
driver.close()