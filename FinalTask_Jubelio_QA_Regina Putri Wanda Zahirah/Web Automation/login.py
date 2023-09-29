from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()

browser.get('https://app.jubelio.com/login')
username = browser.find_element(By.NAME, 'email')
username.send_keys("qa.rakamin.jubelio@gmail.com")
print("Berhasil mengisi email")
password = browser.find_element(By.NAME, 'password')
password.send_keys("Jubelio123!"+ Keys.RETURN)
print("Berhasil mengisi password")
time.sleep(5)
get_url = browser.current_url
if get_url == "https://app.jubelio.com/home":
  print("Berhasil login ke dashboard")