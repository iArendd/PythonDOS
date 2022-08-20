import criarArquivoOpcoes

def gerarArquivo():

    gerarArquivoEscolha = input(str("\nO arquivo que você deseja criar será inserido na pasta raiz, você deseja inserir em uma pasta específica? Digite S para sim ou N para não.\n"))

    if gerarArquivoEscolha == "N":
        
        return criarArquivoOpcoes.opcaoNAO()

    elif gerarArquivoEscolha == "S":

        return criarArquivoOpcoes.opcaoSIM()


    else:
        print("Nada")

    #arquivo = open("pastasCriadas/contatos.txt", "a")
    #arquivo.write("Ola, mundo!")
