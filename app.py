import os
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

	
