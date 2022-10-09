# to decimal number
import re 

def convert_to_digit(c : str):
    my_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    }
    
    return my_dict[c]


def to_decimal(x : str, system: int):
    """
    Converts x to decimal number
    """
    system = float(system)
    res = float(0)

    match = re.search(r',', x)

    str1 = str2 = ""

    if (match != None):
        ind = match.span()[0]
        str1 = x[ind-1::-1]
        str2 = x[ind+1:]
    else:
        str1 = x[::-1]
    
    p = float(1)
    for val in str1:
        res += convert_to_digit(val) * p
        p *= system
    

    p = float(1)/system
    for val in str2:
        res += convert_to_digit(val) * p
        p /= system


    return res