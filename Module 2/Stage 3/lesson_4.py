from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()
    alert = browser.switch_to.alert.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    res = math.log(abs(12*math.sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(res)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()