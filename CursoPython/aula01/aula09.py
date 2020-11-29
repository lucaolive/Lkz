"""
Operador Relacionais
"""

print(2 == 2)  # questiona se é igual ou não
print(2 >= 2)  # pergunta se é maior ou igual

# num recebe o valor
num1 = input("numero1: ")
num2 = input("numero2: ")

# converte "str" para "int"
num1 = int(num1)
num2 = int(num2)

expressao = (num1 == num2)
if expressao == True:
    print("São iguais")
else:
    print("São diferentes")
