#pip install pandas - arquivos
#numpy
#openpyxl

#pip install pyautogui
    #pyautogui.write -> digita algo
    #pyautogui.click -> clica com o botão direito do mouse
    #pyautogui.press -> pressiona uma tecla
    #pyautogui.hotkey -> aperta conjunto de teclas

import pyautogui as pa
import time


pa.PAUSE = 0.5


#Abrir navegador
pa.press("win")
pa.write("opera")
pa.press("enter")

#Abrir Sistema da empresa 
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(2)
pa.click(x=1056, y=355)
pa.write("eugostodagiogio@gmail.com")
pa.press("tab")
pa.write("12345678")
pa.press("enter")
time.sleep(1)

#Importar Base de Dados
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Cadastrar produto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    pa.click(x=1220, y=236)
    pa.write(codigo)
    
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "marca"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "tipo"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "categoria"]))

    pa.press("tab")
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "custo"]))
  
    pa.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pa.write(obs)

    pa.press("tab")
    pa.press("enter")
    pa.scroll(5000)

