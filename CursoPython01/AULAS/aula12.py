num1 = input("primeiro numero: ")
num2 = input("segundo numero: ")

# isnumeric isdigit isdecimal
# checagem de números e positivos
print(num1.isnumeric())
print(num2.isnumeric())

# utilizando a checagem
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Digite um número")
