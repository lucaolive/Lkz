"""
while
"""
"""
# FizzBuzz
x = 0

while x < 100:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x = x + 1

print("End! ")
"""

while True:
    print()
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    operador = input("Enter an operator: ")

    if not num1.isnumeric() or not num2.isnumeric():
        print("You need enter real numbers!")
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "/":
        print(num1 / num2)
    elif operador == "*":
        print(num1 * num2)
    else:
        print("Unavailable Operator!")

