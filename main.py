from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

df = pd.read_excel('challenge.xlsx')

# service = Service(executable_path="msedgedriver.exe")
# driver = webdriver.Edge(service=service)

# Drive mais atualizados
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rpachallenge.com/")

def preencher_formulario(dados):
    campos = {
        "First Name": '//*[@ng-reflect-name="labelFirstName"]',
        "Last Name": '//*[@ng-reflect-name="labelLastName"]',
        "Company Name": '//*[@ng-reflect-name="labelCompanyName"]',
        "Role in Company": '//*[@ng-reflect-name="labelRole"]',
        "Address": '//*[@ng-reflect-name="labelAddress"]',
        "Email": '//*[@ng-reflect-name="labelEmail"]',
        "Phone Number": '//*[@ng-reflect-name="labelPhone"]'
    }
    
    for campo, seletor in campos.items():
        print(f"Preenchendo o campo '{campo}'...{dados[campo]}")
        try:
            input_element = WebDriverWait(driver, 10).until(
                # Usando o XPATH para melhorar precisão
                EC.presence_of_element_located((By.XPATH, seletor))
            )
            input_element.clear()
            input_element.send_keys(dados[campo])
        except Exception as e:
            print(f"Erro ao preencher o campo '{campo}': {e} ")
    
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit" and @value="Submit"]'))
        )
        submit_button.click()
    except Exception as e:
        print(f"Erro ao enviar o formulário: {e}")


if __name__ == "__main__":
    # melhorando performace com o apply
    df.apply(preencher_formulario, axis=1)
    driver.quit()
