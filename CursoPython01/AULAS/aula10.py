"""
Operadores Logicos
"""
""" Verdadeiro E Verdadeiro
comparação1 and comparação2

# Verdadeiro OU Verdadeiro
comparação1 or comparação2"""

a = 2
b = 3

if b > a:
    print("B é maior do que A")
else:
    print("A é maior do que B")

c = "Lucas"

if not c:
    print("Preencha o valor C")
else:
    print(f"Você digitou {c}")

nome = "Lucas Alexandre"

if "Alexandre" not in nome:
    print("Não encontrado!")
else:
    print("Encontrado!")
    print(f"Você digitou {nome}")