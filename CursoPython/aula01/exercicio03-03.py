nome = input("Write your name: ")
qtd = nome.__len__()

if qtd <= 4:
    print("Seu nome é curto")
elif qtd > 4 and qtd < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
