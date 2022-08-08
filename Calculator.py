print("SIMPLE CALCULATOR")
operation = input("Choose operation:\n"
                  "1. Addition:\n"
                  "2. Subtraction:\n"
                  "3. Multiplication:\n"
                  "4. Division\n")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operation == "1":
    result = num1 + num2
    print("Result: ", result)
elif operation == "2":
    result = num1 - num2
    print("Result: ", result)
elif operation == "3":
    result = num1 * num2
    print("Result: ", result)
elif operation == "4":
    result = num1 / num2
    print("Result: ", result)
else:
    print("Wrong operation!")
