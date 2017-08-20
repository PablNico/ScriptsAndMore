def polinomio(valor=10001011, base=2): #Fórmula: V = v*b**vetor
    pos = len(str(valor))
    stvalor = list(str(valor))
    nvalor = 0
    for i in range(pos):
        nvalor += int(stvalor[i])*(base**(pos-1))
        pos -= 1
    print(nvalor)
polinomio()


'''Descobri que a cada 0 colocado no fim do binário dobra o valor, e a cada 1 no final dobra o valor e acrescenta + 1
Ex: 100 = 4
    1000 = 8
    10001 = 17
    100010 = 34
    1000101 = 69
    10001011 = 139

'''