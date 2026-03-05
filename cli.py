from calculator import Calculator

calc = Calculator()

def calculate(a, op, b):
    if op == "+":
        return calc.add(a, b)
    elif op == "-":
        return calc.subtract(a, b)
    elif op == "*":
        return calc.multiply(a, b)
    elif op == "/":
        return calc.divide(a, b)
    else:
        raise ValueError("Invalid operator")