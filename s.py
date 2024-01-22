from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://google.com')

try:
    reject_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div')
    reject_button.click()
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium Python')
    search_box.submit()
except Exception as e:
    print("Fehler beim Klicken des Ablehnungsbuttons:", e)
