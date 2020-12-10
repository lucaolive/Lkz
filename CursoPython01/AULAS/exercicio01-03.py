intnum = input("Write a number: ")

if intnum.isnumeric():
    intnum = int(intnum)
    if intnum % 2 == 0:
        print(f"The númber {intnum} is par.")
    else:
        print(f"The number {intnum} is impar.")
else:
    print("Error, please write a number. ")
