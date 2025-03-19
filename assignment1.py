
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
operation = input("Select +, -, *, /: ")

def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

if operation == "+":
    result = Add(x, y)
elif operation == "-":
    result = Subtract(x, y)
elif operation == "*":
    result = multiply(x, y)
elif operation == "/":
    result = division(x, y)
else:
    result = "Invalid operation selected."

print(result)
        