from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("/Users/zehui/Desktop/Universidad/Python/cripto/chromedriver")

driver.get("https://www.temporary-mail.net/")
sleep(2)
driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[1]/ul/li[1]/a").click()
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])

driver.get("https://www.peregrinoteca.com/_users/register")
sleep(2)

# Creación de cuenta

email = "prueba8@gmail.com"

driver.find_element(By.ID, 'email').send_keys(Keys.COMMAND, 'v')
driver.find_element(By.NAME, 'password1').send_keys('Password123456789,')
driver.find_element(By.NAME, 'password2').send_keys('Password123456789,')
driver.find_element(By.XPATH, '//*[@id="div-label-leido_condiciones"]/div[1]/div/label/span').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="envio"]').click()
sleep(2)

driver.save_screenshot("creacion_eu.png")


# Inicio de sesión

sleep(5)
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/div/a[4]').click()
sleep(2)
driver.find_element(By.ID, 'email1').send_keys(Keys.COMMAND, 'v')
sleep(2)
driver.find_element(By.ID, 'password1').send_keys('Password123456789,')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="envioimagen-login1"]').click()
sleep(2)
driver.save_screenshot("inicio_eu.png")


# Cambio de contraseña

driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/div/a[1]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="carro-compra"]/div[2]/ul/li[3]/a').click()
sleep(2)
driver.find_element(By.NAME, 'newuser_pass').send_keys('Password123456789-')
driver.find_element(By.NAME, 'newuser_pass2').send_keys('Password123456789-')
sleep(5)
driver.find_element(By.XPATH, '//*[@id="envio"]').click()
sleep(2)
driver.save_screenshot("cambio_eu.png")


# Reestablecer contraseña

sleep(5)
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="preheader"]/div/div[1]/div/a[4]').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div/p/a/span').click()
sleep(2)
driver.find_element(By.ID, 'email').send_keys(Keys.COMMAND, 'v')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="envio"]').click()

driver.save_screenshot("reestablecer_eu.png")


driver.switch_to.window(driver.window_handles[0])
sleep(1)
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/ul/li[2]/a').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/a').click()
sleep(2)
driver.back()
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/a').click()
driver.save_screenshot("mail_eu.png")
sleep(2)
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td/table/tbody/tr[2]/td/div/ul/li/a').click()
sleep(2)
driver.find_element(By.NAME, 'password1').send_keys('NewPassword123456789-')
driver.find_element(By.NAME, 'password2').send_keys('NewPassword123456789-')
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/form/div[3]/div/div[1]/button').click()
driver.save_screenshot("reestablecer2_eu.png")


