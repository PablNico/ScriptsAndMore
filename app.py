"""import os
contagem = 28
while True:
	print("Digite os dados necessários e tecle enter")
	print('Digite "sair" para fechar o programa')
	patente = input("Digite a patente: ")
	matricula = input("Matrícula: ")
	nome = input("Digite o nome:")
	contagem+=1
	info = "Informação n° {}-2018-13°BBM".format(contagem)
	texto = '''
	{}
		1. Solicitação em que o {} Mtcl {} {}, da 3ª/13°BBM – Tijucas, pleiteia a inserção no Sistema do Curso de Condutores de Veículo de Emergência – 60 h/a – SENASP. 
			
			2. INFORMAÇÃO:
			a.  Amparo do requerente
			Está amparado pela Portaria n° 12-14-DE, de 21 novembro de 2014.

			b. Estudo fundamentado
			1) Dados informativos sobre o requerente: {} Mtcl {} {}, da 3ª/13°BBM – Tijucas, pleiteia a inserção no Sistema do Curso de Condutores de Veículo de Emergência – 60 h/a – SENASP. 

			2) Apreciação:
			Pela inserção do Curso concluído no SENASP.

			3. PARECER:
			Pelo deferimento, conforme legislação vigente.

		'''.format(info, patente, matricula, nome, patente, matricula, nome)
	
	print(texto)
	
"""

import os

def cria_pastas(i):
	pwd = "{}/Scripts".format(os.getcwd())
	os.system("mkdir -p {}".format(pwd))
	arq = "{}/{}.txt".format(pwd, i)
	return arq

def cria_texto(patente, matricula, nome, num):
	nam = "\t{}\n\n".format(num)
	msg ="{} Mtcl {} {}, da 3ª/13°BBM – Tijucas, pleiteia a inserção no Sistema do Curso de Condutores de Veículo de Emergência – 60 h/a – SENASP. ".format(patente, matricula, nome)
	texto = '''
	{} 
	\t\t1. Solicitação em que o {}
	\t\t\t2. INFORMAÇÃO:
	\t\t\ta.  Amparo do requerente
	\t\t\tEstá amparado pela Portaria n° 12-14-DE, de 21 novembro de 2014.

	\t\t\tb. Estudo fundamentado
	\t\t\t1) Dados informativos sobre o requerente: {}

	\t\t\t2) Apreciação:
	\t\t\tPela inserção do Curso concluído no SENASP.
	\t\t\t3. PARECER:
	\t\t\tPelo deferimento, conforme legislação vigente.

	'''.format(nam,msg,msg)
	return texto

def grava_arquivo(texto, arq):
	fim = open("{}".format(arq), "w")
	fim.write(texto)
	fim.close()
def mostrar():
	print('''
*******************************************************
* Esse script gera um texto com os dados preenchidos, *
* inserindo eles no modelo.						   *
* 													   * 
* Para sair presione CTRL+C 						   *
*******************************************************
''')

if __name__ == '__main__':
	mostrar()
	i=1
	num = int(input("Digite o número: "))
	while True:
		patente = input("Digite a Patente: ")
		matricula = input("Digite a matrícula:")
		nome = input("Digite o nome: ")
		grava_arquivo(cria_texto(patente, matricula, nome, num), cria_pastas(i))
		i+=1
		num+=1


		



	
