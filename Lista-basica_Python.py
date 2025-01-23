'''
Lista de frutas
'''
from operator import index

frutas = ["maçã", "laranja", "melancia", "abacate"]

print(f"As frutas são : {frutas}")

print()
#acesso ao elemento
print(f"A fruta da posição : {frutas[0]}")
print(f"A fruta da posição : {frutas[2]}")
print(f"A fruta da posição : {frutas[3]}")

print()
# adicionar no final da lista
frutas.append("UVA")
print(f"Temos mais frutas : {frutas}")

print()
#Para remover remove() , pop() ou del
#frutas.pop remove o ultimo
#del frutas[1] remove pelo indice
frutas.remove("laranja" )
print(f" Novas frutas : {frutas}")
