from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox(executable_path="")
browser.get("https://play2048.co/")

start = browser.find_element_by_class_name("restart-button").click()
started = browser.find_element_by_tag_name("body")

while True:
    started.send_keys(Keys.DOWN)
    started.send_keys(Keys.LEFT)
    started.send_keys(Keys.UP)
    started.send_keys(Keys.RIGHT)
    
    try:
        browser.find_element_by_class_name("game-over").click()
    
    except NoSuchElementException as Exception:
        pass
