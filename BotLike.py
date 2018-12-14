from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import pyautogui


class Instagram(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.browser = webdriver.Firefox()
        
    def login(self):
        self.browser.get("https://www.instagram.com/")
        sleep(2)
        connect = self.browser.find_element_by_link_text("Conecte-se").click()
        sleep(3)
        user = self.browser.find_element_by_name("username")
        user.send_keys(self.email)
        passw = self.browser.find_element_by_name("password")
        passw.send_keys(self.password)
        passw.submit()
    
    def like(self):
        sleep(7)
        #procura pelo o 'explore'
        explore = self.browser.find_element_by_class_name(
            """glyphsSpriteSafari__outline__24__grey_9.u-__7""")
        #clica no 'explore'
        explore.click()
        sleep(3)
        #procura pela imagem
        hrefs = self.browser.find_elements_by_tag_name("a")
        href = [h.get_attribute("href") for h in hrefs]
        imgs = [img for img in href if img[26:30] == 'p/Br']
        print(len(imgs))
        for a in imgs:
            try:
                #abri a imagem
                self.browser.get(a)
                #botão curtir
                dá_like = self.browser.find_element_by_class_name(
                    """dCJp8.afkep.coreSpriteHeartOpen._0mzm-""")
                #curti a imagem
                dá_like.click()
            except ElementClickInterceptedException:
                print("Falhou")


user = str(input("Email: "))
senha = str(input("Senha: "))
insta = Instagram(user, senha)
insta.login() 
insta.like()