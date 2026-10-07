operador = 0

while operador != 2:

    print("=============================================")

    print("Controle de Gato/Financeiro")

    print("=============================================")

    print("1 - Informar Renda Mensal")
    print("2 - Cadastrar gasto mensal ")
    print("3 - Consultar gastos mensal")
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
            case 1:
                
                renda = float(input("Informe sua renda:\n"))
                
            case 2:
                
                print("Categoria")
                print("1-Alimentação")
                print("2-Saúde")
                print("3-Transporte")
                print("4-Lazer")
                print("5-Outros")

                categoria = int(input("Selecione uma categoria: "))

                match categoria:

                    case 1:

                        print("Alimentação")
                        nome_categoria = "Alimentação"
                        
                    case 2:

                        print("Saúde")
                        nome_categoria = "Saúde"
                    
                    case 3:

                        print("Transporte")
                        nome_categoria = "Transporte"

                    case 4:

                        print("Lazer")
                        nome_categoria = "Lazer"

                    case 5:

                        print("Outros")
                        nome_categoria = "Outros"

                    case _:

                        print("Inválido")
                
                valorGasto = float(input("Digite o valor do gasto"))

            case 3:

                print("Seus gastos:")
                print(f"Categoria: {nome_categoria}")
                print(f"Valor: {valorGasto}")
                
            case 4:

                saldo = renda-valorGasto
                print(f"Seu saldo é: {saldo}")

                if saldo > 0 :

                    print("Saldo Positivo")
                    saldo_status = "Saldo Positivo"

                elif saldo == 0 :

                    print("Sem Saldo")
                    saldo_status = "Sem Saldo"

                else :

                    print("Saldo Negativo")
                    saldo_status = "Saldo Negativo"
                    
            case 5:

                print("Suas estatísticas")
                print(f"Renda: {renda}")
                print(f"Gasto: {valorGasto}")
                print(f"Saldo: {saldo}")
                print(f"Situação do Saldo: {saldo_status}")
                
                
            case 6:
                print("Até Mais")
                operador = 2
            case _:
                print("Opção Inválida")


