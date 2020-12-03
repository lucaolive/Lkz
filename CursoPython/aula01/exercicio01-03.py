intnum = input("Write a number: ")

if intnum.isnumeric():
    intnum = int(intnum)
    if intnum % 2 == 0:
        print(f"O número {intnum} é par.")
    else:
        print(f"o número {intnum} é impar.")
else:
    print("Error, please write a number.")
