import criaPasta


def escolherOpcao():
    escolha = input(str("\nDigite um comando para ser executado. Caso não conheça os comandos, digite --help para listar as funcionalidades: \n"))

    if(escolha == "createFolder"):
        criaPasta.gerarPasta()

    