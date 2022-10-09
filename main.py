# main

import users_input
import to_10_system
import from_decimal

system = users_input.enter_system()
x, y = users_input.enter_numbers(system)

print(f"The chosen system: {system}\nEntered numbers: {x}, {y}")

x = to_10_system.to_decimal(x, system)
y = to_10_system.to_decimal(y, system)
