#  Calculator
# r -> raw string - keep \ / * symbols literal
print(r"""  
   /=================================\
   |   PY🐍THON   CALCULATOR          |
   |---------------------------------|
   |  7   8   9   +   \              |
   |  4   5   6   -   /              |
   |  1   2   3   *   \              |
   |  0   .   =   ÷   /              |
   \=================================/
""")


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "//":
        return num1 // num2
    elif operation == "%":
        return num1 % num2
    else:
        return "Invalid operation"


def calculator():
    num1 = float(input("What is the first number?\n"))
    while True:
        operation = input("Pick an operation (+, -, *, /, //, %):\n").strip()
        num2 = float(input("What is the next number?\n"))
        result = calculate(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(
            f"Type 'y' to continue with {result}, or 'n' to start new:\n").lower().strip()
        if choice == "y":
            num1 = result
        else:
            num1 = float(input("What is the first number?\n"))


calculator()
