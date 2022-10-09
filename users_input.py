# users input

def enter_system():
    """
    Asks user to enter the number system (from 2 to 16)
    """
    while True:
        try:
            users_input = input("Enter a number system (from 2 to 16): ")
            # Check if user have entered exactly one int value: 
            (x,) = tuple(map(int, users_input.split()))
        except:
            print('Incorrect input! Please, try again.')
            continue
        else:
            if x in list(range(2, 17)):
                return x
            else:
                print('The system number must be from 2 to 16! Please, try again.')
                continue

    return 0


def in_system(x : str, system : int):
    """
    Checks if x belongs to number system 'system'
    """
    
    return True

def enter_numbers(system : int):
    """
    Asks user to enter two numbers in the chosen system
    """
    while True:
        try:
            users_input = input("Enter a two numbers in the chosen system: ")
            # Check if user have entered exactly two values: 
            (x, y) = tuple(map(str, users_input.split()))
        except:
            print('Incorrect input! Please, try again.')
            continue
        else:
            if in_system(x, system) and in_system(y, system):
                return x, y
            else:
                print("The entered value isn't in the chosen system! Please, try again.")
                continue

    return 0, 0