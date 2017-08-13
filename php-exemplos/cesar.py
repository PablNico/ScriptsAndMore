def cipher():
    while True:
        palavra = []
        frase = input("Frase a criptografar: " )
        if frase.lower() == 'sair':
            break
        rotacao = int(input("Rotação: "))
        if rotacao > 26:
            print("Digite um numéro até 26")
        else:
            for i in range(len(frase)):
                letra = ord(frase[i])+rotacao
                if letra > 122:
                    letra = 97 + (rotacao//2)
                palavra.append(chr(letra))
        print(''.join(palavra))


cipher()
