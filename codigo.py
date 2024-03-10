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
# print(tabela)


for linha in tabela.index:

	pyautogui.click(x=502, y=290)

	codigo = tabela.loc[linha, "codigo"]
	pyautogui.write(codigo)
	pyautogui.press("tab")

	pyautogui.write(tabela.loc[linha, "marca"])
	pyautogui.press("tab")

	pyautogui.write(tabela.loc[linha, "tipo"])
	pyautogui.press("tab")

	pyautogui.write(str(tabela.loc[linha, "categoria"]))
	pyautogui.press("tab")

	pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
	pyautogui.press("tab")

	pyautogui.write(str(tabela.loc[linha, "custo"]))
	pyautogui.press("tab")

	obs = tabela.loc[linha, "obs"]
	if not pandas.isna(obs):
		pyautogui.write(obs)
	pyautogui.press("tab")

	pyautogui.press("enter")
	pyautogui.scroll(10000)




