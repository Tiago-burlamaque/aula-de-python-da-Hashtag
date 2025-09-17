import pyautogui
import time

pyautogui.PAUSE = 0.8

# Dica: Sempre começar com o código em português, como Exemplo:

# passo 1: Entar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/tabela
# Abrir o janelinha inicial do windows
pyautogui.press("win")
# Digitar Google Chrome 
pyautogui.write("chrome")
# Entrar no Google Chrome
pyautogui.press("enter")
# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# Entrar no site
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# passo 2: Fazer Login
pyautogui.click(x=489, y=428)
pyautogui.write("Autismo@gmail.com")
pyautogui.press("tab")
pyautogui.write("Autismo123")
pyautogui.press("tab")
pyautogui.press("enter")


# passo 3: Importar a base de dados
# passo 4: Cadastrar 1 produto
# passo 5: Repetir para todos os produtos

# pyautogui -> Fazer automações com python

# baixar pacote no cmd -> pip install pyautogui

# -----------------------------------------------------------------------------------------------------

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla do teclado
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas(teclas de atalhos)

