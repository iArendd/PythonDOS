import helpScript

import criaPasta
import criaArquivo

escolha = input(str("\nDigite um comando para ser executado. Caso não conheça os comandos, digite --help para listar as funcionalidades: \n"))

def escolherOpcao(escolha):

    if(escolha == "--help"):
        helpScript.helpComands()
        escolha = input(str("\nDigite um comando para ser executado. Caso não conheça os comandos, digite --help para listar as funcionalidades: \n"))
        escolherOpcao(escolha)
        print("\n======================================================")
        escolha = ""
        escolha = input(str("\nDigite um comando para ser executado. Caso não conheça os comandos, digite --help para listar as funcionalidades: \n"))
        escolherOpcao(escolha)

    else:
    
        match escolha:

            case "--createFolder":
                return criaPasta.gerarPasta()

            case "--createFile":
                return criaArquivo.gerarArquivo()

escolherOpcao(escolha)




    