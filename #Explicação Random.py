# Importa o módulo random para gerar números aleatórios
import random 

numero_secreto = random.randint(1, 100)  # Gera um Nº aleatório entre 1 e 100 e o armazena em Nº secreto
tentativas = 0 # Inicializa o contador de tentativas 

print(numero_secreto)


while True: # Inicia o loop inifinito que continuará até que o número correto seja adivinhado

    palpite = int(input("Digite o seu palpite: ")) # Pede ao usuário para inserir um palpite e converte para inteiro
    tentativas += 1 # Incrementa o contador de tentativas

    if palpite < numero_secreto: # Verifica se o palpite é menor que o nº secreto

        print("O Número secreto é maior. Tente novamente!") # Informa ao usuário que o numero secreto é maior
        
    elif palpite > numero_secreto: # Verifica se o palpite é menor que o nº secreto


        print("O número secreto é menor. Tente novamente!") # Informa ao usuário que o numero secreto é menor

    else: # Se o plapite não for nem maior, nem menor, ele deve ser igual
        
        print("Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.") # Imprime uma mensagem de sucesso

        break # Sai do loop, já que o número correto foi adivinhado. 