expression = input("Enter an arithmetic expression (e.g., 7 * 9): ")
parts = expression.split()  

num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

print("Result:", result)
