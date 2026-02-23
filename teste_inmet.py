from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument('--start-maximized')

try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://portal.inmet.gov.br/')
    print('Sucesso!')
    time.sleep(3)
finally:
    if 'driver' in locals():
        driver.quit()
