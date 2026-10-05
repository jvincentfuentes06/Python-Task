print ("Python Assignment - Simple Calculator")
num1 = float(input("Enter First Number:"))
operator = input("Enter Operator (+, -, *, /): ")
num2 = float(input("Enter Second Number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print ("Sorry, number cannot divide by zero.")
        exit()
    result = num1 / num2
else:
    print("Sorry, Invalid operator")
    exit()

print("Result:", result)
