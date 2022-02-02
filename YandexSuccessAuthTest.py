from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YandexAutomate():

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe')
    
    def login(self, email, password):
        self.browser.get('https://passport.yandex.ru/auth/add?origin=home_yandexid&retpath=https%3A%2F%2Fyandex.ru&backpath=https%3A%2F%2Fyandex.ru')
        #Ввод Email
        self.browser.find_element_by_xpath('//input[@data-t="field:input-login"]').send_keys(email)
        #Клик на подтверждение
        self.browser.find_element_by_xpath('//button[@data-t="button:action:passp:sign-in"]').click()
        #Ввод пароля
        WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@data-t="field:input-passwd"]')
            )
        ).send_keys(password)
        #Клик на подтверждение
        self.browser.find_element_by_xpath('//button[@data-t="button:action:passp:sign-in"]').click()



if __name__ == '__main__':
    yandex = YandexAutomate()
    yandex.login('testname.tests@yandex.ru','28025b716778')
