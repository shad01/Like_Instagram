from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from time import sleep

email = str(input("Email: "))
password = str(input("Senha: "))
print()

browser = webdriver.Firefox()
browser.get("https://twitter.com/login")

send_email = browser.find_element_by_class_name("js-username-field").send_keys(email)
send_pass = browser.find_element_by_class_name("js-password-field")
send_pass.send_keys(password)
send_pass.submit()

sleep(10)
for t in range(1, 11):
    try:
        trending = browser.find_element_by_xpath(f"/html/body/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/ul/li[{t}]")
        print(f"Tweet {t}: {trending.get_attribute('data-trend-name')}")

    except NoSuchElementException:
        pass
