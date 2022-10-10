# main

import users_input
import to_10_system
import from_decimal

def calculate(x, y, operation : str):
    """
    Calculates x operation y
    """
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y


system = users_input.enter_system()
x, y, operation = users_input.enter_expression(system)
x_0, y_0 = x, y

x = to_10_system.to_decimal(x, system)
y = to_10_system.to_decimal(y, system)

result = calculate(x, y, operation)
result = from_decimal.from_decimal(result, system)

print(f"In {system} system: {x_0} {operation} {y_0} = {result}")


