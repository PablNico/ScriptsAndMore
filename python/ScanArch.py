import os
pasta = input('Diretório: ')
arq = os.listdir(pasta)
save = os.environ['HOMEPATH']
gravar = open(save +'\\Desktop\\arquivos.txt', 'w')

for i in arq:
    gravar.write("_____________________\n"+"\n"+i+"\n"+"_____________________\n")
    print(i)
    try:
        arq = os.listdir("%s/%s" %(pasta, i))
        msg = ("_____________________\n" + ("%s/%s\n" %(pasta, i)) + "_____________________\n")
        msg1 = ("%s/%s/" %(pasta, i))
        print(msg)
        for i in arq:
            gravar.write(msg1 + i + "\n")
            print(msg1+i + "\n")
    except:
        pass
gravar.close()

