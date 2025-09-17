import pyautogui

# Eu quero abrir o terminal
pyautogui.hotkey("Ctrl", "'")
# Eu quero adicionar o projeto no github
pyautogui.write("git add .")
pyautogui.press("enter")
pyautogui.write('git commit -m "Automatizando projeto"')
pyautogui.press('enter')
pyautogui.write("git push")
pyautogui.press("enter")