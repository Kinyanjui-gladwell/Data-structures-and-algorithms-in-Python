""" Convert a string of roman numbers to an integer without exceptions """
def roman_to_int(string):
    dict_of_roman = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D':500, 'M':1000}
    i = 0
    integer = 0
    while (i<len(string)):
        if string[i] in dict_of_roman:
            integer += dict_of_roman[string[i]]
            i += 1
        else:
            print('string is not in roman numerals')
    print(integer)
roman_to_int('II')
roman_to_int('XXV')
roman_to_int('MMMDCX')