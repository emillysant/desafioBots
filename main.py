from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

df = pd.read_excel('challenge.xlsx')

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://rpachallenge.com/")

def preencher_formulario(dados):
    campos = {
        "First Name": 'input[ng-reflect-name="labelFirstName"]',
        "Last Name": 'input[ng-reflect-name="labelLastName"]',
        "Company Name": 'input[ng-reflect-name="labelCompanyName"]',
        "Role in Company": 'input[ng-reflect-name="labelRole"]',
        "Address": 'input[ng-reflect-name="labelAddress"]',
        "Email": 'input[ng-reflect-name="labelEmail"]',
        "Phone Number": 'input[ng-reflect-name="labelPhone"]'
    }
    
    for campo, seletor in campos.items():
        print(f"Preenchendo o campo '{campo}'...{dados[campo]}")
        try:
            input_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
            )
            input_element.clear()
            input_element.send_keys(dados[campo])
        except Exception as e:
            print(f"Erro ao preencher o campo '{campo}': {e} ")
    
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"][value="Submit"]'))
        )
        submit_button.click()
    except Exception as e:
        print(f"Erro ao enviar o formulário: {e}")

for index, row in df.iterrows():
    print()
    print(f"Processando dados do registro {index+1}...")
    print()
    preencher_formulario(row)
    time.sleep(2) 

driver.quit()