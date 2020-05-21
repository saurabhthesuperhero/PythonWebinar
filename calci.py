# Program make a simple calculator


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", x + y)

        elif choice == '2':
            print(x, "-", y, "=", x - y)

        elif choice == '3':
            print(x, "*", y, "=", x * y)

        elif choice == '4':
            print(x, "/", y, "=", x / y)
        break
    else:
        print("Invalid Input")