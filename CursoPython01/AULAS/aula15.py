"""
Manipulação de strings
"""
# positivos [0123456789]
#        012345678
texto = "Python s2"
#        ^^^^^^^^^
#       -987654321

print(texto[5])

# negativos -[987654321]
url = "www.google.com/"
print(url[:-5])
print(url[0:7])
print(url[4:10])
print(url[-6])

# pulando casas
texto2 = "Lucas Alexandre"
print(texto2[0:5:2])
# do caractere 0 ao 5 de 2 em 2

print(len(texto2))
print(len(texto))
print(len(url))
