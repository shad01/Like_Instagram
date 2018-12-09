from time import sleep
from selenium import webdriver
import pyautogui


class Instagram(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.browser = webdriver.Firefox()
        
    def login(self):
        self.browser.get("https://www.instagram.com/")
        sleep(3)
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
            """Szr5J.kIKUG.coreSpriteDesktopNavExplore""")
        #clica no 'explore'
        explore.click()
        sleep(3)
        i = 0 
        g = 1
        while True:
            try:
                sleep(2)
                i += 1
                #procura pela imagem
                img = self.browser.find_element_by_xpath(f"""/html/body/span/
                    section/main/div/article/div[1]/div/div[{g}]/div[{i}]""")
                #clica na imagem encontrada
                [img.click() for x in range(2)] 
                sleep(1)
                #Dá o like na foto 
                dá_like = self.browser.find_element_by_class_name(
                    """dCJp8.afkep.coreSpriteHeartOpen._0mzm-""").click()
                if i == 3:
                    i = 0
                    g += 1
            except Exception:
                print("Falhou")
            finally:
                #utiliza o botão de voltar do browser
                self.browser.back()
                #faz o scroll(boto do meio do mouse) descer
                pyautogui.scroll(-300)
                

user = str(input("Email: "))
senha = str(input("Senha: "))
insta = Instagram(user, senha)
insta.login()
insta.like()