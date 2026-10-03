operador = 0

while operador != 2:

    print("=============================================")

    print("Controle Financeiro")

    print("=============================================")

    print("1 - Informar Renda Mensal")
    print("2 - Cadastrar gasto")
    print("3 - Consultar gastos")
    print("4 - Consultar situação financeira")
    print("5 - Ver estatísticas")
    print("6 - Sair")

    print("=============================================")

    valido = 0
    while valido == 0: 

        entrada = input("Digite a opção: ")

        valido = 1

        for i in range(len(entrada)):
            caractere = entrada[i]
            if not('0' <= caractere <= '9'):
                print("Inválido, Tente Novamente \n")
                valido = 0
                break

    if valido == 1:
        escolha = int(entrada)
        
        match escolha:
            #case 1:
            #case 2:
            #case 3:
            #case 4:
            #case 5:
            case 6:
                print("Até Mais")
                operador = 2
            case _:
                print("Opção Inválida")


