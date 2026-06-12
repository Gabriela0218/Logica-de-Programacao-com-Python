"""
Exercício:

Crie um algoritmo que solicite ao usuário uma senha, e só sai do 
looping do While quando for digitado a senha corretamente
"""


SenhaSystem = "123456"

senhaDigitada = input("Digite sua senha: ")

while (SenhaSystem != senhaDigitada):

    print ("Senha incorreta, tente novamente!")

    SenhaDigitada = input("Digite sua senha: ")

print("Muito bem! você digitou a senha correta!")    