import os

def gerarPasta():
    nomePasta = str(input("Digite o nome da pasta a ser criada\n"))
    os.makedirs('./pastasCriadas/' + nomePasta)

    print("\nA pasta {} foi criada com sucesso dentro do diretório específico chamado 'pastasCriadas'\n".format(nomePasta))



'''CRIAR DIRETÓRIO'''


#os.makedirs(nomeDiretorio)

#os.makedirs('trabalho01/' + nomePasta)


'''EXECUTAR ARQUIVO'''


