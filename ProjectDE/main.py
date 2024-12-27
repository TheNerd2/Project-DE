import os
import requests
from colorama import Fore, init, Back, Style
import ipscanner

init(autoreset=True)

#Codigo do MENU do PROJECT DE
def menu():
	print(Style.BRIGHT + Fore.RED + '''\n

██████  ██████   ██████       ██ ███████  ██████ ████████     ██████  ███████ 
██   ██ ██   ██ ██    ██      ██ ██      ██         ██        ██   ██ ██      
██████  ██████  ██    ██      ██ █████   ██         ██        ██   ██ █████   
██      ██   ██ ██    ██ ██   ██ ██      ██         ██        ██   ██ ██      
██      ██   ██  ██████   █████  ███████  ██████    ██        ██████  ███████ 
	options:
	1 = ip scanner
	2 = port scanner
	3 = People Database(Informations) 
	4 = report bugs in this project! 
''')

def escolha():
	opcoes = input("Escolhe uma opção:")
	if opcoes == "1":
	 abrir()

def abrir():
	with open('ipscanner.py','r') as arquivo:
		dandoread = arquivo.read()
		exec(dandoread, globals()) #global context mais ou menos

menu()
escolha()
input("pressione qualquer key para sair do CMD/POWERSHELL")