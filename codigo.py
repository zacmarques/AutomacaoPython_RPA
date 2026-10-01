#-*- coding: utf-8 -*-   
#sempre que for começar um código tem que pensar: como eu faria para resolver esse problema manualmente?
#Esse procedimento é o passo-a-passo do programa, a lógica do programa
#Passo 1: entrar no sistema da empresa
#Passo 2: Fazer login no sistema, e-mail e senha
#Passo 3: Acessar a base de dados
#Passo 4: Cadastrar o primeiro produto
#Passo 5: Repetir o passo quatro até o final da lista
#Agora você traduz isso para Python
#Tem a biblioteca Selenium que vai automizar em segundo plano (que é oq eu preciso), mas só funciona no Navegador (não funfa em app no desktop ent vira usar esse autogui)

import pyautogui
import time
import pandas
import openpyxl
 
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #Serviço fake só para teste de cadastro
email = "emailtestepython.com"
senha = "senhadificilteste"
tabela = pandas.read_csv("E:\coisas-do-zac\Faculdade_textos_emprego\Disciplinas_EAD_Certificados\Python_Hashtag\Aula 1\Aula 1 - Automações de Tarefas e Bots\Aula 1 - Automações de Tarefas e Bots\produtos.csv")
#Passo 1: entrar no sistema da empresa. Abrir navegador e entrar no site
pyautogui.press("win")
pyautogui.write("Brave")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) #Aqui a pausa tem que ser um pouco maior por conta da velocidade de internet variar
#Passo 2: Fazer login. Aqui eu uso duas variaveis declaradas, mas poderia ser .write
pyautogui.click(x=415, y=367)
pyautogui.write(email)
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
#Passo 3: Acessar a base de dados
print(tabela)
#Passo 4 e 5: Cadastrar primeiro produto e repetir até acabar tabela
for linha in tabela.index:
    pyautogui.click(x=388, y=261)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #código
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #Marca
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #tipo
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #Categoria
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #Preço_unitario
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #Custo
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) 
    pyautogui.press("tab")
    #OBS
    pyautogui.press("enter")
    #voltar para o início da tela
    pyautogui.scroll(5000)