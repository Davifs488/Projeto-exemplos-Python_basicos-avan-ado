'''
Informar se o numero e par ou impar
'''

numero = int(input(" Digite um numero "))

resultado = "par" if numero % 2 == 0 else "impar"

print(f" O numero é {numero} ele é {resultado}")



print("Preciso de mais informações ")

nome = input("Inform seu nome : ")

idade = int(input(" Informe sua idade : "))

resposta = "Maior de idade " if idade >= 18 else "menor de idade "

print(f" {nome} você é {resposta} tem {idade} de idade e o  numero anterior é {resultado}")

