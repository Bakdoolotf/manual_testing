from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class GoogleAutomate():

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe')
    
    def request_(self,search):
        self.browser.get('https://www.google.ru/')
        #Поле поиска
        self.browser.find_element_by_name('q').send_keys(search)
        #Подтверждение поиска
        self.browser.find_element_by_name('q').send_keys(Keys.RETURN)
        # проверка на ссылку www.mvideo.ru 
        try:
            self.browser.find_element_by_xpath('//a[@href="https://www.mvideo.ru/products/kofeinaya-stanciya-bork-c804-4000182"]').click()
            print('www.mvideo.ru - Есть' )
        except:
            print("отсутствует")
        self.browser.quit()
        


if __name__ == '__main__':
    for i in range(11):
        google = GoogleAutomate()
        google.login('купить кофемашину bork c804')
        print(i)



