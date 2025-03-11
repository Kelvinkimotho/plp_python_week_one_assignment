print("*** Welcome to kelvin's calculator ****")
# user input for the first number
num1 = float(input("Enter the first number: "))

# user input for the second number
num2 = float(input("Enter the second number: "))

#  user input for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Then here i can perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operation == '-':
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operation == '*':
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operation == '/':
    if num2 != 0: #number two must not be zeor because there will be a zero error
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Error because you are trying to divide the first number with a zero which is mathematically wrong")
else:
    print("Invalid operation, choose a valid operation (+,*,-,/)")