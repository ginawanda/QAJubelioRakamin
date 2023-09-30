from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser = webdriver.Chrome()

browser.get('https://app.jubelio.com/login')
username = browser.find_element(By.NAME, 'email')
username.send_keys("qa.rakamin.jubelio@gmail.com")
print("Berhasil mengisi email")
password = browser.find_element(By.NAME, 'password')
password.send_keys("Jubelio123!"+ Keys.RETURN)
print("Berhasil mengisi password")
time.sleep(2)
browser.get('https://app.jubelio.com/home/inventory')
print("Membuka halaman inventory")
browser.find_element(By.XPATH, "//*[text()='Penyesuaian Persediaan']").click()
print("Click penyesuaian persediaan")
time.sleep(3)
harapPilih = browser.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/span/div/span")
actions = ActionChains(browser)
actions.double_click(harapPilih).perform()
print("Memilih produk")

time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div[1]').click()
time.sleep(4)
quantity = browser.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/span/div/div')
actions.double_click(quantity).perform()
actions.double_click(quantity).perform()
# time.sleep(3)

# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]/div[5]')))
# inputQty = browser.find_element(By.XPATH, '//*[@id="page-top"]/div[5]/div/input')
# inputQty.send_keys("10"+ Keys.RETURN)
print("Mengubah quantity")

time.sleep(5)
browser.find_element(By.XPATH, "//*[text()='Simpan']").click()
print("Berhasil menyimpan perubahan inventory")
time.sleep(3)