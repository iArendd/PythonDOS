import os


def opcaoNAO():

    nomeArquivo = input(str("\nDigite o nome do arquivo a ser criado:\n"))
    formatoArquivo = input(str("\nDigite a extenção do tipo do arquivo a ser criado:\n"))

    arquivo = open(nomeArquivo+"."+formatoArquivo, "a")

    print("O arquivo {}.{} foi criado com sucesso.".format(nomeArquivo, formatoArquivo))



    print("\n===============================================================\n")



    escreverArquivo = input(str("Você deseja escrever alguma informação dentro do arquivo? Digite S para sim ou N para não:\n"))

    if escreverArquivo == "S":

        descricaoArquivo = input(str("Escreva o que deve ser inserido no arquivo:\n"))
        arquivo.write(descricaoArquivo)

        print("\nA descrição '{}' foi inserida com sucesso.\n".format(descricaoArquivo))

    elif escreverArquivo == "N":
        print("Programa encerrado.")
        print("===============================================================\n")


#---------------------------------------------------------------------------------

def opcaoSIM():

    nomeDiretorio = input(str("\nDigite o diretório da pasta que você deseja criar o arquivo. Exemplo: 'primeiraPasta/segundaPasta/terceiraPasta/' \n"))

    nomeArquivo = input(str("\nDigite o nome do arquivo a ser criado:\n"))
    formatoArquivo = input(str("\nDigite a extenção do tipo do arquivo a ser criado:\n"))

    arquivo = open(nomeDiretorio+nomeArquivo+"."+formatoArquivo, "a")

    print("O arquivo {}.{} foi criado com sucesso no diretorio {}.".format(nomeArquivo, formatoArquivo, nomeDiretorio))



    print("\n===============================================================\n")

    

    escreverArquivo = input(str("Você deseja escrever alguma informação dentro do arquivo? Digite S para sim ou N para não:\n"))

    if escreverArquivo == "S":

        descricaoArquivo = input(str("Escreva o que deve ser inserido no arquivo:\n"))
        arquivo.write(descricaoArquivo)

        print("\nA descrição '{}' foi inserida com sucesso.\n".format(descricaoArquivo))

    elif escreverArquivo == "N":
        print("Programa encerrado.")
        print("===============================================================\n")

