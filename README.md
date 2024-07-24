# Projeto de Automação com Selenium

## Descrição

Este projeto é uma aplicação de automação web que preenche formulários em um site de desafio usando Selenium. O objetivo é preencher automaticamente campos de um formulário com dados de um arquivo Excel e enviar o formulário para cada linha de dados.

## Estrutura do Projeto

- `main.py`: Script principal que contém a lógica para preencher o formulário e enviá-lo.
- `challenge.xlsx`: Arquivo Excel contendo os dados a serem inseridos no formulário.
- `msedgedriver.exe`: Driver necessário para o Selenium interagir com o Microsoft Edge.

## Bibliotecas Utilizadas

- `selenium`: Biblioteca para automação de navegadores web.
- `pandas`: Biblioteca para manipulação e análise de dados em Python.
- `openpyxl`: Biblioteca para ler e escrever arquivos Excel (.xlsx).

## Instruções de Instalação e Execução

### 1. Clonar o Repositório

Clone este repositório para sua máquina local usando o seguinte comando:

```bash
git clone <URL do Repositório>
cd <Nome do Repositório>
```

### 2. Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

``` python -m venv venv ```

Ative a venv no Windows:

``` venv/Scripts/activate ```

### 3. Instalar as Dependências

``` pip install -r requirements.txt ```

## Rodado projeto

[![Assista ao vídeo no YouTube](https://img.youtube.com/vi/zbQdW0BX1w8/0.jpg)](https://youtu.be/zbQdW0BX1w8?autoplay=1)


## Melhorias

Entre na branch melhorias:
<ol>
    <li>Usando o navegador do chrome por ser mais atualizado</li>
    <li>Usando o apply no lugar do iterrows para melhorar performace</li>
    <li>Trocando Css por Xpath na busca para ter mais precisão</li>
</ol>
