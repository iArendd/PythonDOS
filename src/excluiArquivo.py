import os

#os.rmdir('trabalho01/diretorioDoArquivo')

def excluirArquivo():

    trigger = True

    while(trigger):

        nomeDiretorio = input(str("\nDigite o caminho do diretório onde se encontra o arquivo a ser excluído:\n"))

        print("\nOs arquivos no diretório '{}' são os seguintes:\n".format(nomeDiretorio))

        print("==============================================================")

        for root, dirs, files in os.walk(nomeDiretorio, topdown=False):
            for name in files:
                print(os.path.join(root, name))

            for name in dirs:
                print(os.path.join(root, name))

        print("==============================================================")

        aceitarDiretorio = input(str("\nEsse é o diretório desejado? Digite S para sim ou N para não:\n"))

        if aceitarDiretorio == "S":
            
            trigger = False

        elif aceitarDiretorio == "N":
            trigger = True

        else:
            print("Comando inválido!")
            trigger = True

    

    nomeArquivo = input(str("Digite o nome do arquivo com seu formato no qual você deseja remover:\n"))


    if os.path.isfile(nomeDiretorio+nomeArquivo):
        os.remove(nomeDiretorio+nomeArquivo)
    else:    
        print("Erro: O arquivo '{}' não existe no diretório '{}'".format(nomeArquivo, nomeDiretorio))