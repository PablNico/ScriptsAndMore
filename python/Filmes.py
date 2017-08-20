import requests
import json

def procurar_filme(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo)
        requisicao = json.loads(req.text)
        return requisicao
    except:
        msg = "ERRO"
        return msg

def printar_detalhes(filme):
    print("")
    print('Filme: ' + filme['Title'])
    print('Ano: ' + filme['Year'])
    print('Diretor: ' + filme['Director'])
    print('Elenco: ' + filme['Actors'])
    print('Nota: ' + filme['imdbRating'])
    print("")
sair = False
while not sair:
    op = input("Digite um filme ou SAIR: ")
    if op.upper() == 'SAIR':
        sair = True
    else:
        filme = procurar_filme(op)
        if filme['Response'] != 'False':
            printar_detalhes(filme)
        else:
            print("\nFilme inválido\n")
            
