import os

def gerarArquivo():

    gerarArquivoEscolha = input(str("\nO arquivo que você deseja criar será inserido na pasta raiz, você deseja inserir em uma pasta específica? Digite SI para sim ou NO para não.\n"))

    if gerarArquivoEscolha == "NO":
        
        nomeArquivo = input(str("\nDigite o nome do arquivo a ser criado:\n"))
        formatoArquivo = input(str("\nDigite a extenção do tipo do arquivo a ser criado:\n"))

        arquivo = open(nomeArquivo+"."+formatoArquivo, "a")

        print("O arquivo {}.{} foi criado com sucesso.".format(nomeArquivo, formatoArquivo))

    else:
        print("Nada")

    #arquivo = open("pastasCriadas/contatos.txt", "a")
    #arquivo.write("Ola, mundo!")
