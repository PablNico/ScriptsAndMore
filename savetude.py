import os

# script para criar arquivos de texto rápido em vez de postar no face

while True:

	os.system('clear')
	texto = input("Pode escrever:\n")
	titulo = input("Nome do arquivo: ")

	arq = open("/var/www/html/Site/txts/%s" %titulo,'w')

	arq.write(texto)
	arq.close
	escolha = input("Continuar? [S/n]")
	if escolha.lower() == "n":
		break