import math
try:
    operator = (input("Enter an operator (+, -, *, /, **, %, !): ").strip().lower())
    if operator == "!":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = math.factorial(n)
        print(f"Result: {n}! = {result}")
    elif operator in ("+", "-", "*", "/", "**", "^" "%"):
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator in ("**", "^"):
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        print(f"Result: {num1} {operator} {num2} = {result}")
    else:
        raise ValueError(f"Invalid operator '{operator}'.")
except ValueError as e:
    if "could not convert" in str(e) or "invalid literal" in str(e):
        print("Error:Invalid number! Please enter valid numeric values.")
    else:
        print(f"Error: {e}")
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero!")
except OverflowError:
    print("Error: The result is too large to compute!")