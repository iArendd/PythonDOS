from genericpath import isdir
import os
import shutil


def excluirPasta():

    nomeDiretorio = input(str("\nDigite o diretório junto com a pasta que você deseja excluir, exemplo: ../pastaPrincipal/pastaSecundaria/pastaParaRemover\n"))

    if isdir(nomeDiretorio) == True:

        if len(os.listdir(nomeDiretorio)) == 0:
            os.rmdir(nomeDiretorio)
        else:    
            shutil.rmtree(nomeDiretorio)

    else:
        print("Esse diretório não existe.")