from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


driver = webdriver.Chrome("/Users/zehui/Desktop/Universidad/Python/cripto/chromedriver")

driver.get("https://www.peregrinoteca.com/_users/register")
sleep(2)

email = 'fuerzabruta3@gmail.com'
# Creación de cuenta

driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.NAME, 'password1').send_keys('Password123456789,')
driver.find_element(By.NAME, 'password2').send_keys('Password123456789,')
driver.find_element(By.XPATH, '//*[@id="div-label-leido_condiciones"]/div[1]/div/label/span').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="envio"]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/div/a[4]').click()


def inicio(password):
    sleep(2)
    driver.find_element(By.ID, 'email1').send_keys(email)
    driver.find_element(By.ID, 'password1').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="envioimagen-login1"]').click()


def base26(largo):
    chars = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    clave = ""
    for i in range(largo):
        clave += random.choice(chars)
    return clave  

driver.get("https://www.peregrinoteca.com/_users/register")
for i in range(100):
    inicio(base26(15))