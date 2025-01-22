def exibi_informa(**kwargs):

    for chave, valor in kwargs.items():

        print(f"{chave}: {valor}")

exibi_informa(nome="Mariana", idade=25, cidade="São Paulo")

print()

exibi_informa(nome="Jão", profissao="Analista")

print()

exibi_informa(nome="Dava_dev", nota="10", profissao="Desenvolvedor" )