import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_first():

    """
    TK-235. Тест запуска браузера
    """
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized") #open Browser in maximized mode
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url="https://testqastudio.me/")

#menu-top [class*= 'menu-item-11088'
element = driver.find_element(by=By.CSS_SELECTOR, value='#menu-top [class*="menu-item-11088"]')
element.click()

assert driver.current_url == 'https://testqastudio.me/fag/', 'Unexpected url'

faq_menu_2 = driver.find_element(by=By.XPATH, value='//*[contains(text(), "Можно ли поставить доп.фурнитуру?")]')
faq_menu_2.click


assert True, ''   





