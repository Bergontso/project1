from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('/home/alexander/Загрузки/chromedriver')
driver = webdriver.Chrome(service=s)
# Сайт Интернет-банк Санкт-Петербург должен открыться
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
time.sleep(1)
# Изменяем размер окна
driver.set_window_size(1440, 900)
time.sleep(1)
# Нажимаем кнопку Вход по имени и паролю
driver.find_element(By.ID, "login-button").click()
# Нажимаем кнопку Вход поcле подтверждения кода из СМС
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(1)
# Переходим в раздел Карты
driver.find_element(By.ID, "cards-overview-index").click()
time.sleep(1)
# Проверяем средства на карте Travel
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10068']/ul/li[2]/a").click()
time.sleep(1)
# Проверяем последние операции по карте Travel
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10068']/ul/li[3]/a").click()
time.sleep(1)
# Открываем карту Золотая
driver.find_element(By.XPATH, "//*[@id='cards']/li[1]/ul/li[2]/a/div/div/div[1]/span").click()
time.sleep(2)
# Проверяем средства на карте Золотая
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10069']/ul/li[2]/a").click()
time.sleep(1)
# Проверяем последние операции по карте Золотая
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10069']/ul/li[3]/a").click()
time.sleep(1)
# Выходим из интернет-банка
exitbutton = driver.find_element(By.ID, "logout-button")
time.sleep(1)
if exitbutton is None:
    print("Элемента нет")
else:
    print("Элемент есть.\nТест пройден успешно!")
