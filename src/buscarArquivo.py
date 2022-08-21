import os
from pathlib import Path



def encontrarArquivo():

    count = 1

    nomeDiretorio = input(str("\nDigite o diretório no qual você deseja buscar o arquivo desejado:\n"))
    nomeArquivo = input(str("\nDigite o nome do arquivo que você deseja encontrar:\n"))

    print("--------------------------------------------------------")
    print("\n Buscando arquivo com o nome: '{}' .........\n".format(nomeArquivo))

    try:

        print("===============ARQUIVOS ENCONTRADOS===================\n")
        print("--------------------------------------------------------")

        for root, subFolder, files in os.walk(nomeDiretorio):

            for file in files:

                if nomeArquivo in file:

                    print("{}: {}/ {}".format(count, root, file))
                    print("--------------------------------------------------------")

                    count = count + 1

        print("\n=======================================================\n")

    except:

        print("\nNão foi possível concluír a execução pois houve algum erro.\n")
