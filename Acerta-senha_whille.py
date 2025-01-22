'''
Acerte  a senha
'''

senha_correta = "python"

senha = ""

while senha != senha_correta :

   senha = input(" Digite a senha : ")
   if senha != senha_correta:
       print("Errou digite novamente")
   else:

       print(f"SENHA CORRETA ! ACESSO LIBERADO")