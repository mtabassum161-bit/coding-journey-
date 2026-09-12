#introduction 
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old.")

#simple calculator 

import math

num1 = float(input("Enter first number: "))

operator = input("Enter operator (+, -, *, /, //, %, **, √, sin, cos, tan, log): ")
 
if operator in ["√", "sin", "cos", "tan", "log"]:
     num2 = num1 

else:
    num2 = float(input("Enter second number: "))



if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "**":
    print(num1 ** num2)


elif operator == "*":
    print(num1 * num2)

#if divide by 0

elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)

# Now scientific calculator 

elif operator == "%":
    print(num1 % num2)

elif operator == "//" :
    print(num1 // num2)

elif operator == "√":
    if num1 < 0:
        print("Cannot calculate square root of a negative number")
    else:
        print(math.sqrt(num1))

elif operator == "sin":
    print(math.sin(math.radians(num1)))

elif operator == "cos":
    print(math.cos(math.radians(num1)))

elif operator == "tan":
    print(math.tan(math.radians(num1)))

elif operator == "log":
    if num1 <= 0:
        print("Log is only defined for positive numbers")
    else:
        print(math.log10(num1))

else:
    print("Invalid operator")



