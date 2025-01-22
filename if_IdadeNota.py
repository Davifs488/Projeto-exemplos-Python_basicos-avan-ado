'''
Nome e nota de aprovação
criaça ,jovem, adulto e idoso
'''
nome = input(" Diga seu nome : ")
nt = float(input(" Qual a sua nota : "))

if nt >= 6 :
    print(f" {nome} você está aprovado com a nota {nt}")
elif nt >= 4 :
    print(f" {nome} você está de recuperação sua nota foi {nt}")
else:
    print(f" {nome} você está reprovado sua nota foi {nt}")




idade = int(input("AGORA Digite sua idade :iiii"))

if idade < 12 :
    print(f" {nome} você é uma Criança")

elif idade < 18 :
    print(f"{nome} você é um Adolescente")

elif idade >= 18 and idade < 65 :
    print(f" {nome} você é um Adulto ")

else:
    print(f"{nome} você é um Idoso ")