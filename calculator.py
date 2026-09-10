#introduction 
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old.")

#simple calculator 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator(+,-,*,/): ")

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


