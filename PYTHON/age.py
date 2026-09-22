# Age checker program
user1 = "Please enter your age: "
user2 = "You are older than 18. Please proceed."
user3 = "You are younger than 18. Don't waste my time."

age = int(input(user1))
if age >= 18:
    print(user2)
else:
    print(user3)

# ----------------------------------------------- ---------------- ------
# ----------------------------------------------- ---------------- ------
# Calculator program (+, -, *, /)
calculator = input("Enter the operation you want to perform (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if calculator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif calculator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif calculator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif calculator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from (+, -, *, /).")

# ----------------------------------------------- ---------------- ------
# ----------------------------------------------- ---------------- ------
#Test results program
test_score = float(input("Enter your test score (0-100): "))
if test_score >= 90:
    print("You got an A!")
elif test_score >= 80:
    print("You got a B!")
elif test_score >= 70:
    print("You got a C!")
elif test_score >= 60:
    print("You got a D!")
else:
    print("You got an F!")

# ----------------------------------------------- ---------------- ------
# ----------------------------------------------- ---------------- ------
#Sex checker program. Disclaimer: I was bored, so I made this program to amuse myself. Please don't take it seriously. I am not responsible for any offense caused by this program. This program is meant for entertainment purposes only.
sex = input("Please enter your sex (M/F): ").strip().upper()
toy1 = float(input("Enter the size of your package: "))
if sex == "M":
    print("Enter your package size in inches.")
    if toy1 >= 15:
        print("You are a man with a big package. Proceed to room A1")
    elif toy1 >= 10:
        print("You are a man with a medium package. Not bad! Please enter room A1")
    elif toy1 >= 5:
        print("You are a man with a small package. Please proceed to room A2")
    elif sex == "F":
        print("You are a woman. Please enter room A0, have a seat and enjoy the view!")
    else:
        print("Invalid input. Please enter 'M' for male or 'F' for female.")    

# ----------------------------------------------- ---------------- ------
# ----------------------------------------------- ---------------- ------
#
