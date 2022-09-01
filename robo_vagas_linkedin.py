#pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'.\chromedriver.exe')

browser.get("https://www.linkedin.com/login")

input_email = browser.find_element_by_id("username")
input_email.send_keys('**Seu email aqui**')

input_senha = browser.find_element_by_id("password")
input_senha.send_keys("**Sua senha aqui**")

btn_login = browser.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

busca = browser.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca.send_keys('Objetivo da busca') #seja linguagem de programação ou vaga 
busca.send_keys(keys.RETURN)

time.sleep(3)

filtro.vagas = browser.find_element_by_xpath("//button[@aria-label='Vagas]")
filtro.vagas.click()

input('')

