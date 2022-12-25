from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Foo')
    browser.find_element(By.NAME, 'lastname').send_keys('Foo')
    browser.find_element(By.NAME, 'email').send_keys('Foo')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(10)
    browser.close()
    browser.quit()