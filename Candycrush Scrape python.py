# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:51:45 2022

@author: edukr
"""

from selenium import webdriver # Automatiza o navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import keyboard


print('Starting robot...')
print('Loading Chromedriver (3 instances) and accessing booster webpage...')

boosters=['//*[@id="sendme"]/h6[2]/select/option[2]',
          '//*[@id="sendme"]/h6[2]/select/option[3]',
          '//*[@id="sendme"]/h6[2]/select/option[4]',
          '//*[@id="sendme"]/h6[2]/select/option[5]',
          '//*[@id="sendme"]/h6[2]/select/option[6]',
          '//*[@id="sendme"]/h6[2]/select/option[7]',
          '//*[@id="sendme"]/h6[2]/select/option[8]',
          '//*[@id="sendme"]/h6[2]/select/option[9]',
          '//*[@id="sendme"]/h6[2]/select/option[10]',
          '//*[@id="sendme"]/h6[2]/select/option[11]']

url='https://baronstrainers.com/candycrush/boosters.php'
opcao = Options()
opcao.headless = True
driver = webdriver.Chrome(options=opcao)
driver2 = webdriver.Chrome(options=opcao)
driver3 = webdriver.Chrome(options=opcao)
driver.get(url)
driver2.get(url)
driver3.get(url)
chave=input('Paste your candycrush session id: ')
driver.find_element(By.XPATH,'//*[@id="sendme"]/h6[1]/input').send_keys(chave)
driver2.find_element(By.XPATH,'//*[@id="sendme"]/h6[1]/input').send_keys(chave)
driver3.find_element(By.XPATH,'//*[@id="sendme"]/h6[1]/input').send_keys(chave)



# ENTER THE NUMBER OF CHOOSEN BOOSTER HERE, IN '[]'
driver.find_element(By.XPATH,boosters[8]).click()
driver2.find_element(By.XPATH,boosters[8]).click()
driver3.find_element(By.XPATH,boosters[2]).click()
####


while True:
    time.sleep(3)
    try:
        driver.find_element(By.XPATH,'//*[@id="sendme"]/input[3]').click()
        driver2.find_element(By.XPATH,'//*[@id="sendme"]/input[3]').click()
        driver3.find_element(By.XPATH,'//*[@id="sendme"]/input[3]').click()
        print('Successfully added boosters!')
    except:
        pass
    if keyboard.is_pressed('q'):
        break
print('Exiting...')
driver.close()
driver2.close()
driver3.close()


## XPATH Boosters list
# (0) Hammer: //*[@id="sendme"]/h6[2]/select/option[2]
# (1) Fish: //*[@id="sendme"]/h6[2]/select/option[3]
# (2) UFO: //*[@id="sendme"]/h6[2]/select/option[4]
# (3) Hand: //*[@id="sendme"]/h6[2]/select/option[5]
# (4) Coloured bomb: //*[@id="sendme"]/h6[2]/select/option[6]
# (5) Color wheel: //*[@id="sendme"]/h6[2]/select/option[7]
# (6) Listred and wrapped: //*[@id="sendme"]/h6[2]/select/option[8]
# (7) Brush: //*[@id="sendme"]/h6[2]/select/option[9]
# (8) Party bomb: //*[@id="sendme"]/h6[2]/select/option[10]
# (9) Lucky: //*[@id="sendme"]/h6[2]/select/option[11]


