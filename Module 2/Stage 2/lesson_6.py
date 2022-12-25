from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    res = math.log(abs(12*math.sin(x)))

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, 'answer').send_keys(res)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()



finally:
    time.sleep(10)
    browser.close()
    browser.quit()