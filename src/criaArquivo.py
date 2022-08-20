import criarArquivoOpcoes


def gerarArquivo():

    def decisaoGerarArquivo():

        gerarArquivoEscolha = input(str())
            
        if gerarArquivoEscolha == "N":
            
            return criarArquivoOpcoes.opcaoNAO()

        elif gerarArquivoEscolha == "S":

            return criarArquivoOpcoes.opcaoSIM()

        elif gerarArquivoEscolha == "SAIR":
            print("Programa encerrado.")

        else:
            print("Ação interrompida! Digite um comando válido:")
            return decisaoGerarArquivo()


    gerarArquivoEscolha = print("\nO arquivo que você deseja criar será inserido na pasta raiz, você deseja inserir em uma pasta específica? Digite S para sim / N para não ou SAIR para encerrar.\n")
    decisaoGerarArquivo()

    #arquivo = open("pastasCriadas/contatos.txt", "a")
    #arquivo.write("Ola, mundo!")
