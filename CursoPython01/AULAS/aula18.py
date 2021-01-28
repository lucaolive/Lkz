"""
For in Python
Iterando string com for
"""

texto = "Python"
# com while
c = 0
while c < len(texto):
    print(texto[c])
    c += 1

print("\n")

# com for
for letra in texto:
    print(letra)

print("\n")

"""
Funçao range(start=0, stop, step=1)
"""

for n in range(10):
    print(n)
for n in range(0, 10, 3):
    print(n)
