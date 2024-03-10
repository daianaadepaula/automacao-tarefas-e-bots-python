import pyautogui
import time
import pandas

pyautogui.PAUSE = 7.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(12)

pyautogui.click(x=455, y=410)
pyautogui.write("daianaadepaula1@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaAqui")
pyautogui.click(x=671, y=572)	
time.sleep(12)

tabela = pandas.read_csv("produtos.csv")
print(tabela)


