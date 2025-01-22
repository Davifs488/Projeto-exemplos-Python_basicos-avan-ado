'''
Importe o modulo random para gerar um  número aleatorio
Gere um número aleatorio entre 1 e 20
usar o laço while para o jogo
'''

import random

numero_secreto = random.randint(1, 20)

print(" O numero está entre 1 e 20")

palpite = None

cont = 0

while palpite != numero_secreto :
    cont += 1

    palpite = int(input(" Digite seu palpite : "))

    if palpite > numero_secreto :
       print("Te um numero MENOR")
    elif palpite < numero_secreto :
       print(f"Tente um numero MAIOR")
    else:
       print(f" Você ACERTOU o numero é {palpite} com {cont} tentativas")