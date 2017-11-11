'''Bubble sort'''
import os

def pedirNumeros():
	vetor = []
	while True:
		
		try:
			num = int(input("Digite um valor ou qualquer letra para sair: "))
			vetor.append(num)
		except:
			break
	return vetor

def bubbleSort(vetor):
	if len(vetor) <= 1:
		return vetor
	else:
		for x in range(0, len(vetor)):
			for i in range(0,len(vetor)-1):
				if vetor[i] > vetor[i+1]:
					aux = vetor[i+1]
					vetor[i+1] = vetor[i]
					vetor[i] = aux
	return vetor	
	
def main():
	vetor = pedirNumeros()
	print(bubbleSort(vetor))

main()
		
		