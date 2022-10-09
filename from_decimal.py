# from decimal to system
from math import modf

def convert_from_digit(c : str):
    my_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    }
    
    return my_dict[c]


def from_decimal(x : float, system : int):
    """
    Converts decimal x to the chosen system
    """
    frac, whole = modf(x)
    whole = int(whole)

    res_whole = ""
    
    if whole == 0:
        res_whole = "0"
    else: 
        while whole > 0:
            res_whole = convert_from_digit(whole%system) + res_whole
            whole = whole//system

    res_frac = ""
    if frac < 10**-13:
        pass
    else:
        for i in range(10):
            frac = frac * system
            frac, whole_0 = modf(frac)
            res_frac = res_frac + convert_from_digit(int(whole_0))

            if frac < 10**-13:
                break

    if (res_frac != ""):
        return res_whole + ',' + res_frac
    
    return res_whole