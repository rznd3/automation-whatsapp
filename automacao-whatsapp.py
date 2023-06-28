from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

import pandas as pd

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random


list = []

contatos_df = pd.read_excel("enviando.xlsx")

browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")

while len(browser.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)


for i, number in enumerate(contatos_df['Número']):

    strnumber = str(number)

    for n in strnumber:
        list.append(n)

    test = float(list[-1])

    if test%2 == 0:
        msg = "Oi, tudo bem?. Sou o Gabriel da LearningFun. Somos especializados no ensino de inglês para crianças e queremos apresentar a você nossa proposta para a implementação da nossa metodologia em sua Escola. E assim oferecer aos pais de seus alunos algo relevante para educação dos seus filhos. Tem interesse em nos conhecer?"
        texto = urllib.parse.quote(f"{msg}")
    else:
        msg = "Olá, tudo bem? Sou o Gabriel da LearningFun. Somos especializados no ensino de inglês para crianças. Queremos apresentar a você nossa proposta para a implementação da nossa metodologia em sua Escola e assim oferecer aos pais de seus alunos algo relevante para educação dos seus filhos. Gostaria de nos conhecer melhor?"
        texto = urllib.parse.quote(f"{msg}")

    link = f"https://web.whatsapp.com/send?phone=55{number}&text={texto}"
    browser.get(link)

    while len(browser.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)

        
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')))
        browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)

    except:
        print(number)

    tm = random.randint(73, 88)
    time.sleep(tm)

    