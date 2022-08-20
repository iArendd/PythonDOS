import os


def opcaoNAO():

    nomeArquivo = input(str("\nDigite o nome do arquivo a ser criado:\n"))
    formatoArquivo = input(str("\nDigite a extenção do tipo do arquivo a ser criado:\n"))

    arquivo = open(nomeArquivo+"."+formatoArquivo, "a")

    print("O arquivo {}.{} foi criado com sucesso.".format(nomeArquivo, formatoArquivo))

#---------------------------------------------------------------------------------

def opcaoSIM():
    
    nomeDiretorio = input(str("\nDigite o diretório da pasta que você deseja criar o arquivo. Exemplo: 'primeiraPasta/segundaPasta/terceiraPasta/' \n"))

    nomeArquivo = input(str("\nDigite o nome do arquivo a ser criado:\n"))
    formatoArquivo = input(str("\nDigite a extenção do tipo do arquivo a ser criado:\n"))

    arquivo = open(nomeDiretorio+nomeArquivo+"."+formatoArquivo, "a")

    print("O arquivo {}.{} foi criado com sucesso no diretorio {}.".format(nomeArquivo, formatoArquivo, nomeDiretorio))

