"""
Write a function, which accepts time delta specifier as a string argument and returns time interval
in seconds as an integer.
Supported time units: s – seconds, m – minute, h – hour, d – day, with seconds
being default unit and one being default value. Please supply unit tests for the solution.

Examples of input time delta specifier and output value:

Time Delta Specifier	Output Value
30	                      30
30s	                      30
s	                      1
60.5m	                  3630
10seconds	           Exception raised
1y	                   Exception raised
<empty string>	       Exception raised
"""


def seconds_returner(time_string):
    unit_dict_converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    num_symbol = '.0123456789'
    # If argument is integer, return argument as seconds
    if isinstance(time_string, int):
        return time_string

    num = ''.join(filter(lambda x: x in num_symbol, time_string))
    unit = ''.join(filter(lambda x: x not in num_symbol, time_string))
    #
    if unit in unit_dict_converter.keys() or unit == '':
        return (float(num) if num else 1) * (unit_dict_converter[unit] if unit else 1)

    raise Exception('What the f...')
