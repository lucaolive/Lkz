"""
Formatando valores com modificadores

:s - Texto (str)
:d - IOnteiros (int)
:f - Numero de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
;(CARACTERE)(> ou < ou ^)(QUATIDADE)(TIPO - s, d, f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 5
div = num1 / num2
nome = "Lucas Alexandre"

# ":."
print("{:.2f}".format(div))
print(f"{div:.2f}")

# ":"
print(f"{num1:0>10}")
print(f"{num1:0<10}")
print(f"{num1:0^10}")
print(f"{nome:#^50}")
nome_formatado = "{0:*>20}".format(nome, num1, num2)
#                  ^ = a posição da variavel desejada dentro da função .format
print(nome_formatado)

print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # primeiras letras maiusculas
