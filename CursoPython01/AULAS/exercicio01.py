nome = "Lucas"
idade = 23
altura = 1.79
peso = 92
ano_at = 2020
nascimento = ano_at - idade
imc = peso / (altura ** 2)

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é de {imc:.2f}.")
print(f"{nome} nasceu em {nascimento}.")
