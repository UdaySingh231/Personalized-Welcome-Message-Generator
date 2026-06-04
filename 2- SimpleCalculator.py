# Simple Calculator 

# User will enter two numbers

num1 = float(input("Enter first number \n"))
num2 = float(input("Enter second number"))

# Perform calculations

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2 if num2 != 0 else "Cannot be divided by zero"

# Results will be displayed now 

print(f"Addition of {num1} and {num2} : {add}")
print(f"Subtraction of {num1} and {num2} : {sub}")
print(f"Multiplication of {num1} and {num2} : {multi}")
print(f"Divison of {num1} and {num2} : {div}")