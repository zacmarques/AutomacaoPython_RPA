#-*- coding: utf-8 -*-   
#sempre que for começar um código tem que pensar: como eu faria para resolver esse problema manualmente?
#Esse procedimento é o passo-a-passo do programa, a lógica do programa
#Passo 1: entrar no sistema da empresa
#Passo 2: Fazer login no sistema, e-mail e senha
#Passo 3: Acessar a base de dados
#Passo 4: Cadastrar o primeiro produto
#Passo 5: Repetir o passo quatro até o final da lista

import os
import time
from pathlib import Path
import pandas as pd
import pyautogui
from dotenv import load_dotenv

# ━━ TRAVAS DE SEGURANÇA DO PYAUTOGUI ━━
# Move o mouse para o canto superior esquerdo para interromper a execução em emergências
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# ━━ CARREGAMENTO DE VARIÁVEIS DE AMBIENTE ━━
load_dotenv()
EMAIL = os.getenv("APP_EMAIL", "emailtestepython@dominio.com")
SENHA = os.getenv("APP_PASSWORD", "senhadificilteste")
LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# ━━ CAMINHO RELATIVO SEGURO ━━
# Localiza o arquivo na mesma pasta do script
DIRETORIO_ATUAL = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ARQUIVO_PRODUTOS = DIRETORIO_ATUAL / "produtos.csv"

if not ARQUIVO_PRODUTOS.exists():
    raise FileNotFoundError(f"Arquivo de dados não encontrado em: {ARQUIVO_PRODUTOS}")

tabela = pd.read_csv(ARQUIVO_PRODUTOS)

# ━━ EXECUÇÃO DA AUTOMAÇÃO ━━
# Passo 1: Entrar no sistema
pyautogui.press("win")
pyautogui.write("Brave")
pyautogui.press("enter")
time.sleep(1.5)

pyautogui.write(LINK)
pyautogui.press("enter")
time.sleep(3)  # Aguarda carregamento da página

# Passo 2: Fazer login
# NOTA: Recomenda-se ajustar as coordenadas conforme sua tela
pyautogui.click(x=415, y=367)
pyautogui.write(EMAIL)
pyautogui.press("tab")
pyautogui.write(SENHA)
pyautogui.press("enter")
time.sleep(2)

# Passo 3 e 4: Cadastrar produtos com tratamento de input
for linha in tabela.index:
    pyautogui.click(x=388, y=261)
    
    # Preenchimento tratado de cada campo
    codigo = str(tabela.loc[linha, "codigo"]).replace("\n", "").strip()
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = str(tabela.loc[linha, "marca"]).replace("\n", "").strip()
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = str(tabela.loc[linha, "tipo"]).replace("\n", "").strip()
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"]).replace("\n", "").strip()
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    preco = str(tabela.loc[linha, "preco_unitario"]).replace("\n", "").strip()
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    custo = str(tabela.loc[linha, "custo"]).replace("\n", "").strip()
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs.lower() != "nan" and obs.strip():
        pyautogui.write(obs.replace("\n", " ").strip())
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    # Retorna ao topo
    pyautogui.scroll(5000)
