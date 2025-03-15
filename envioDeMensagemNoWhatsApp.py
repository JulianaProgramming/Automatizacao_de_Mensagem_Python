#Projeto enviar mensagem no whatsapp
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de tecla

# aguardando um tempinho para começar
pyautogui.PAUSE = 0.5

# abrindo o aplicativo (WhatsApp)
pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter")

# aguardando alguns segundos para abrir o aplicativo
time.sleep(7)

# pesquisando o contato no WhatsApp
pyautogui.hotkey("ctrl", "f")
pyautogui.write("Minhas coisas")
time.sleep(2)
pyautogui.press("tab")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)

# clicando na barra para escrever a mensagem
pyautogui.click(x=745, y=1001)
time.sleep(3)

# inicializando o contador para mandar mensagem 
number = 1

# enviando as 3 mensagens seguidas
while number <= 3: 
    pyautogui.write("Oi, tudo bem ")
    pyautogui.press("enter")
    time.sleep(2)
    number = number + 1
