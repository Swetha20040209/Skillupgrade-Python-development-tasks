print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
operation = int(input("Enter the operation: "))
if operation == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum is", num1 + num2)
elif operation == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The difference is", num1 - num2)

elif operation == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The product is", num1 * num2)

elif operation == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 != 0:
        print("The result is", num1 / num2)
    else:
        print("Error: Division by zero is invalid")

else:
    print("Invalid Entry")