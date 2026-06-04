# Number Comparison Tool

# 1 . Get user input two numbers

num1 = float(input("Enter the first number\n"))
num2 = float(input("Enter the second number\n"))

#2 Comparison result

if num1 == num2 :
  print("Both numbers are equal")
if num1 > num2 :
  print(f"{num1} is greater than {num2}")
else :
  print(f"{num1} is smaller than {num2}")  

  # 2. Check whether the number is zero

if num1 ==0 and num2 == 0 :
  print("\n Both numbers are zero")
elif num1 == 0 or num2 == 0:
  print("\n At least one number is zero ")
else:
  print("Both numbers are non zero")