import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.otodom.pl/pl/oferty/sprzedaz/dzialka/plewiska?distanceRadius=15&page=1&limit=36&ownerTypeSingleSelect=ALL&locations=%5Bcities_6-3614%5D&priceMax=200000&areaMin=600&areaMax=1200&plotType=%5BBUILDING%5D&by=DEFAULT&direction=DESC&viewType=listing")
try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "css-p74l73"))
    )
    for element in elements:
        print(element.text)
except:
    print("Element not found")
    driver.quit()


time.sleep(5)
driver.quit()


# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver import Chrome
#
# service = Service(ChromeDriverManager().install())
# browser = Chrome(service=service)
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
#
#
# browser = webdriver.Chrome()
# browser.get('https://httpbin.org/forms/post')
#
# #
# custname = browser.find_element_by_name("custname")
# custname.clear()
# custname.send_keys("Szymon Obara")
