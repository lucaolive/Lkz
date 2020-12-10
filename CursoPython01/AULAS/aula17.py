"""
Função while
"""

#        Indices
#        0123456789.......................33...............
phrase = "The rat gnawed at the clothes of the king of Rome"
size_phrase = len(phrase)
temp = 0
new = ""
upercase = input("Upercase Letter: ")

while temp < size_phrase:
    word = phrase[temp]
    if word == upercase:
        new += word.upper()
    else:
        new += phrase[temp]

    print(new)
    temp += 1
