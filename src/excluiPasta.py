import os

nomeDiretorio = " "
nomeArquivo = "../pastasCriadas/teste1/teste.txt"



if os.path.isfile(nomeArquivo):
    os.remove(nomeArquivo)
else:    ## Show an error ##
    print("Erro: O arquivo '{}' não existe no diretório '{}'".format(nomeArquivo, nomeDiretorio))











'''if(temConteudo == True):
    shutil.rmtree()
'''