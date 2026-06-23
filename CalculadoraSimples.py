# Calculadora Simples

while True:
    print("\nCalculadora Simples: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Receber a escolha do usuário
    escolha = input("Escolha uma operação: ")

    # Condição para sair do programa
    if escolha == "5":
        print("Até mais!")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Condição de Adição
    if escolha == "1":
        resultado = num1 + num2
        print("Resultado", resultado)
    # Condição subtração
    elif escolha == "2":
        resultado = num1 - num2
        print("Resultado", resultado)
    # Condição Multiplicação
    elif escolha == "3":
        resultado = num1 * num2
        print("Resultado", resultado)
    # Condição Divisão
    elif escolha == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado", resultado)
        else:
            print("Erro: Divisão por zero.")
    else:
        print("Tente novamente")



 
    