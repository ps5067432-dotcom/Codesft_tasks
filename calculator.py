print("SIMPLE CALCULATOR")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choices = input("Enter the choice: (+, -, *, /): ")

if choices == "+":
    print("Result =", a + b)

elif choices == "-":
    print("Result =", a - b)

elif choices == "*":
    print("Result =", a * b)

elif choices == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid choice!")