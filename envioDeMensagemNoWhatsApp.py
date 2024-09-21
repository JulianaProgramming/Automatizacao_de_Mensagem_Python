#Projeto enviar mensagem no whatsapp

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# abrir o aplicativo (zap)
pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter")
time.sleep(3)
#pyautogui.click(x=411, y=254) #primeiro fixado
pyautogui.click(x=282, y=292) #segundo fixado(meu grupo UFOP)
pyautogui.press("enter")
time.sleep(3)


# mandar mensagem 
number = 1

while number <= 3: #enviará 3 mensagens seguidas
    pyautogui.write("*Olá, tudo bem ?* ")
    pyautogui.press("enter")
    time.sleep(2)
    number = number + 1