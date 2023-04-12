from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import schedule
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--incognito") # abrir janela anonima
chrome_options.add_argument("--disable-extensions") # desativar extensoes
chrome_options.add_argument("--disable-popup-blocking") # desativar bloqueio de popup
chrome_options.add_argument("--disable-logging") # desativar logging
chrome_options.add_argument("--disable-gpu") # desativar gpu
chrome_options.add_argument("--disable-infobars") # desativar infobars
driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe", options=chrome_options)

driver.get("https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&osid=1&passive=1209600&service=mail&ifkv=AQMjQ7R6iF6IKSshgu0XpTtBnv8fZayQ0rI9h-pXwrhNoCKKOyRNJ7gbP_oAkHM5VBF3o_OHxIcQuA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(2)
LoginGmail = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
LoginGmail.send_keys('costajonas2810@gmail.com')
ContinueGmailConta = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
ContinueGmailConta.click()
time.sleep(2)

SenhaGmail = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
SenhaGmail.send_keys('240681281005')
ContinueSenhaGmail = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
time.sleep(2)
driver.get("https://www.ganharnasredes.com/")
time.sleep(random.uniform(3, 10))

fechar = driver.find_element(By.XPATH, '//*[@id="modalAvisoCurso"]/div/div/div[3]/button')
fechar.click()
time.sleep(random.uniform(1, 3))

botãoAcessar = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div/a[2]')
botãoAcessar.click()
time.sleep(random.uniform(3, 5))

outroFechar = driver.find_element(By.XPATH, '//*[@id="modalAvisoCurso"]/div/div/div[3]/button')
outroFechar.click()
time.sleep(random.uniform(3, 5))

buttonMudarEmail = driver.find_element(By.XPATH, '//*[@id="uname"]')
buttonMudarEmail.send_keys('costajonas2810@gmail.com')
time.sleep(random.uniform(3,5))

Senha = driver.find_element(By.XPATH, '//*[@id="pwd"]')
Senha.send_keys('jonas281005')
time.sleep(random.uniform(3, 5))

login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[3]/button')
login.click()

time.sleep(random.uniform(3,5))

RealizarAçoes = driver.find_element(By.XPATH, '//*[@id="sidebarnav"]/li[9]/center/a')
RealizarAçoes.click()

time.sleep(random.uniform(3, 5))

Iniciar = driver.find_element(By.XPATH, '//*[@id="btn_iniciar"]')
Iniciar.click()

time.sleep(random.uniform(3, 5))

def BotInst():
    try:
        if "Seguir" in driver.page_source:
            # Clicar no botão "Seguir"
            seguir = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Od"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button')
            seguir.click()
        elif "Curtir" in driver.page_source:
            # Clicar no botão "Curtir"
            curtir = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Od"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div/div/div[1]/div/article[1]/div/div[3]/div/div/section[1]/span/button/div[2]/span/svg')
            curtir.click()
        else:
            # Se não houver botão de "Seguir" ou "Curtir", sair do loop
            print("Não há botão de 'Seguir' ou 'Curtir'.")
            return False
    except Exception as e:
        print("Erro: ", e)
        return False
    return True

