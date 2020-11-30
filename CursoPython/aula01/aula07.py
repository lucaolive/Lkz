"""
Entrada de dados
"""
nome = input("Qual seu nome? ")  # input sempre retorna string
anos = input("Qual a sua idade: ")
nascimento = 2020-int(anos)  # mudando a variavel anos de "str" para "int"

print(f"o usuario digitou {nome} e o tipo da variavel é "
      f"{type(nome)}")
print(f"{nome} tem {anos} anos.")
print(f"{nome} nasceu em {nascimento}.")
