'''
Calculadora com função
'''

def multiplicao(a, b):
    return a * b


def subtracao(a, b) :
    return a - b

def soma(a, b):
    return a + b


def subtracao(a, b):
    if b != 0 :
        return a / b
    else:
        return "ERRO : Divisão por zero não é permitido ."


print("Escolha uma operação")
print("1. Multiplicacao")
print("2. Subtração")
print("3. Soma")
print("4. divisão")

operacao = input(" Digite o número da operação desejada  =  1 | 2 | 3 | 4")

num1= float(input(" Digite o primeiro número : "))
num2= float(input(" Digite o segundo numero : "))

if operacao == "1":

    resultado = multiplicao(num1 , num2)

    print(f" resultado da multiplicação é : {resultado}")

elif operacao == "2":

    resultado = subtracao(num1 , num2)

    print(f" Resultado da subtação : {resultado}")

elif operacao == "3":

    resultado = soma(num1, num2)

    print(f" Resultado da soma : {resultado}")


elif operacao == "4":

    resultado = subtracao(num1, num2)

    print(f" Resultado da subtracao : {resultado}")

else:
    print(" Operação invalida")

