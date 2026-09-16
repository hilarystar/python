try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError(f"Invalid operator '{operator}'. Please use +, -, *, or /.")
    print(f"Result: {num1} {operator} {num2} = {result}")
except ValueError as e:
    if "could nit convert" in str(e):
        print("Error:Invalid number! Please enter valid numeric values.")
    else:
        print(f"Error: {e}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")