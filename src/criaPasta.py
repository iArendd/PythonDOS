import os

def gerarPasta():
    nomePasta = str(input("Digite o nome da pasta a ser criada\n"))
    os.makedirs('pastasCriadas/' + nomePasta)

    print("A pasta "+nomePasta+" foi criada com sucesso dentro do diretório específico chamado 'pastasCriadas'")



'''CRIAR DIRETÓRIO'''


#os.makedirs(nomeDiretorio)

#os.makedirs('trabalho01/' + nomePasta)


'''EXECUTAR ARQUIVO'''


