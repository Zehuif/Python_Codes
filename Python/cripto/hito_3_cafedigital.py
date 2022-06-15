from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome("/Users/zehui/Desktop/Universidad/Python/cripto/chromedriver")
driver.get("https://www.temporary-mail.net/")
sleep(2)
driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[1]/ul/li[1]/a").click()
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])

driver.get("https://cafedigital.cl/mi-cuenta/")
sleep(2)

# Creación de cuenta

driver.find_element(By.ID, 'reg_email').send_keys(Keys.COMMAND, 'v')
sleep(2)
driver.find_element(By.ID, 'reg_password').send_keys('Password123456789,')
driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button').click()
sleep(2)

# Inicio de sesión

sleep(5)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/nav/ul/li[6]/a').click()
sleep(2)
driver.find_element(By.ID, 'username').send_keys(Keys.COMMAND, 'v')
sleep(2)
driver.find_element(By.ID, 'password').send_keys('Password123456789,')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button').click()
sleep(2)
driver.save_screenshot("inicio_ch.png")


# Cambio de contraseña

driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/nav/ul/li[5]/a').click()
sleep(2)
driver.find_element(By.ID, 'account_first_name').send_keys('nombre')
driver.find_element(By.ID, 'account_last_name').send_keys('apellido')
driver.find_element(By.ID, 'password_current').send_keys('Password123456789,')
driver.find_element(By.ID, 'password_1').send_keys('Password123456789-')
driver.find_element(By.ID, 'password_2').send_keys('Password123456789-')
sleep(5)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/div/form/p[5]/button').click()
sleep(2)
driver.save_screenshot("cambio_ch.png")



# Reestablecer contraseña

sleep(5)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/nav/ul/li[6]/a').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[4]/a').click()
driver.find_element(By.ID, 'user_login').send_keys(Keys.COMMAND, 'v')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/form/p[3]/button').click()
sleep(1)
driver.save_screenshot("reestablecer_ch.png")

driver.switch_to.window(driver.window_handles[0])
sleep(1)
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/ul/li[2]/a').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/a').click()
sleep(2)
driver.back()
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/a').click()
sleep(2)
driver.save_screenshot("mail_ch.png")

driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/p[5]/a').click()
sleep(2)
driver.find_element(By.ID, 'password_1').send_keys('NewPassword123456789-')
driver.find_element(By.ID, 'password_2').send_keys('NewPassword123456789-')
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/form/p[4]/button').click()
driver.save_screenshot("reestablecer2_ch.png")
