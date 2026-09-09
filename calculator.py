
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old.")



num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "**":
    print(num1 ** num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Invalid operator")

roll_numbers = [101, 105, 102, 101, 108, 105, 110]

unique_roll_numbers = set(roll_numbers)

print("Unique roll numbers:", unique_roll_numbers)

def odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

odd_even(7)