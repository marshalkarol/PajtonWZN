from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-notifications')

service = Service("C:/Users/karol/Desktop/studia/1 stopień/chrome selenium webdriver/chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.reddit.com/r/ChuckNorris/')
#coś poniżej średnio działa, ale nie mam czasu naprawić
# button = driver.find_element(By.CSS_SELECTOR, 'SHORTCUT_FOCUSABLE_DIV > div:nth-child(6) > div._3q-XSJ2vokDQrvdG6mR__k > section > div > section._2BNSty-Ld4uppTeWGfEe8r > section:nth-child(1) > form > button')
# time.sleep(5)
# button.click()

# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'SHORTCUT_FOCUSABLE_DIV > div:nth-child(6) > div._3q-XSJ2vokDQrvdG6mR__k > section > div > section._2BNSty-Ld4uppTeWGfEe8r > section:nth-child(1) > form > button')))
# button.click

# for _ in range(10):
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

for _ in range(10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

time.sleep(1000)

driver.quit()
driver.close()