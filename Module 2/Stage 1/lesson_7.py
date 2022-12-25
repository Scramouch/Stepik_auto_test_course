from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(link)

    box = browser.find_element(By.ID, 'treasure')
    x = box.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    print(x)

finally:
    time.sleep(10)
    browser.close()
    browser.quit()