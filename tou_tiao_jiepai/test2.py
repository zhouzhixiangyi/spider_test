from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
browser.get('https://www.toutiao.com/')
input = browser.find_element_by_class_name('tt-input__inner')
input.send_keys('街拍')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser,10)
browser.switch_to_window(browser.window_handles[1])
print(browser.current_url)
browser.find_element_by_class_name()


