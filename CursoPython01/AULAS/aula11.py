"""
contagem \\ len
"""

string1 = input("digite aqui, texto1: ")
string2 = input("digite aqui, texto2: ")
qtd = len(string1+string2)

print(string1 + string2, " ", qtd, "caracteres")

print(string1.__len__() + string2.__len__(), "Caracteres")
