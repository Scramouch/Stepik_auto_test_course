from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser.get(link)

    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    z = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(z))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()

