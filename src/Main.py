import helpScript

import criaPasta
import criaArquivo
import excluiArquivo
import excluiPasta
import buscarArquivo
import comandoInvalido


versionScript = str("v.0.1.0")


escolha = input(str("\nDigite um comando para ser executado. Caso não conheça os comandos, digite --help para listar as funcionalidades: \n"))


if(escolha == "--version"):

    print("\nVersão do código: {}\n".format(versionScript))

elif(escolha == "--help"):

    helpScript.helpComands()

elif(escolha == "--stop"):

    print("Programa encerrado.")

elif(escolha == "--createFolder"):

    criaPasta.gerarPasta()

elif(escolha == "--createFile"):

    criaArquivo.gerarArquivo()

elif(escolha == "--deleteFile"):

    excluiArquivo.excluirArquivo()

elif(escolha == "--deleteFolder"):

    excluiPasta.excluirPasta()

elif(escolha == "--findFile"):

    buscarArquivo.encontrarArquivo()

else:

    print("Comando inválido!")
