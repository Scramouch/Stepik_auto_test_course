from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/cats.html'
    browser.get(link)
    browser.find_element(By.ID, "button")

finally:
    time.sleep(10)
    browser.close()
    browser.quit()