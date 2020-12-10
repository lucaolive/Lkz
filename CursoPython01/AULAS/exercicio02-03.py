hora = input("Write the time (0-23): ")

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print("Please, Write a time in beetween 0 and 23.")
    else:
        if hora <= 11:
            print("Bom dia!")
        elif hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
else:
    print("Please, Write a time in beetween 0 and 23.")

