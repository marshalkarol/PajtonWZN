from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--dissable-notifications')

service = Service("C:\Users\karol\Desktop\studia\1 stopień\chrome selenium webdriver\chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.fizyka.pw.edu.pl/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni')

elements = driver.find_elements(By.CSS_SELECTOR, 'h2, h2 + div')
for element in elements:
    print(element.text)


driver.close()