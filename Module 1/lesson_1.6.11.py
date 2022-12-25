from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input.first:required')
    input1.send_keys('Foo')

    input2 = browser.find_element(By.CSS_SELECTOR, 'input.second:required')
    input2.send_keys('Foo')

    input3 = browser.find_element(By.CSS_SELECTOR, 'input.third:required')
    input3.send_keys('Foo')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
