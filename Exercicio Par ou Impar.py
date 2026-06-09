#exercicio Par ou Impar
#Crie um algoritmo que solicite a entrada de um número positivo e inteiro e imprima se o
#número é par ou impar


n1 = int(input( "Insira um numero"))

verificaNumero = n1 % 2  #Resto da divisão

if verificaNumero == 0:
    print(f"O número {n1} é PAR")

else:
    print(f"O número {n1} é ÍMPAR")