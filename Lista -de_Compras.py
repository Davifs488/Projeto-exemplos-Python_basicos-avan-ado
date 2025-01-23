'''
Criar um programa que possa ser usado  como
uma list de produtos, e possa colocar e excluir produtos
'''

def exibir_menu():
    print("\n Menu")
    print("1. Adicionar um item")
    print("2. Remover um item")
    print("3. Listar todos os intens")
    print("4. Sair")

compras = []

def adcionar_item():

    item = input("Digite o nome do item para adicionar : ")

    compras.append(item)

    print(f"O item '{item}' foi adicionado á lista ")


def remover_item():

    item = input("Digite o nome do item para  remover : ")

    if item in compras :

        compras.remove(item)

        print(f" O item '{item}' foi removido da lista")
    else:
        print(f" O item '{item}' não está na lista .")


def listar_itens():

    if len(compras) > 0 :

        print("Itens na lista de compras : ")

        for i, item in enumerate(compras):

            print(f"{i+1}. {item}")

    else:

        print("A lista de compras está vazia ")


while True :

    exibir_menu()

    opcao = input("Escolha uma opção : ")

    if opcao == "1" :

        adcionar_item()

    elif opcao == "2" :

        remover_item()

    elif opcao == "3" :

        listar_itens()

    elif opcao == "4" :

        print("Saindo do programa .")

        break

    else:

        print("Opção invalida ! Por favor, escolha uma opção válida")



