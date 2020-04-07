from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import time

class Bot:
    def __init__(self):
        self.mensagem = "Ei"
        self.contato =["Arisnaldo"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    def EnviarMensagens(self):    
        #<span dir="auto" title="EU SOZINHO " class="_1wjpf _3NFp9 _3FXB1">EU SOZINHO </span>

        #<div tabindex="-1" class="_1Plpp">
        print('Rodando')
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        
        contato = self.driver.find_element_by_xpath("//span[@title='Arisnaldo']")
        time.sleep(3)
        contato.click()
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        chat_box.click()
        time.sleep(3)
        chat_box.send_keys(self.mensagem)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(5)

bot = Bot()
bot.EnviarMensagens()