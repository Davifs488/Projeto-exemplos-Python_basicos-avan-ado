'''
A dicionar uma lista com itens de compras comuns.
Esta lista contém itens como "pão", "leite", "ovos"
'''
#Solicita ao usuário que digite o nome de um item que está
#procurando na lista de compras
#A FUNÇÃO '' inpt() '' capttura a entrada do cusuário  com o uma string
#A FUNÇÃO  '' lower() '' é apliccaado á string de entrada para converter
#todos os caaracteres em minúscuas,

lista_compras = ["pão", "leite", "ovos"]
item = input(" Digite um item que está na compra " ).lower()

if item in lista_compras:
    print(f" {item.capitalize()} está na lista de  compras .")
else:
    print(f" {item.capitalize()} não está na lista de  compras .")

