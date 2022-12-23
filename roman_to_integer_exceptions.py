def roman_to_int(string):
    dict_of_roman = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D':500, 'M':1000}
    i = 0
    integer = 0
    while (i<len(string)):
        if not string[i] in dict_of_roman:
            print('string is not in roman numerals')
        else:
            s1 = dict_of_roman[string[i]]
            if i + 1 < len(string):
                s2 = dict_of_roman[string[i+1]]
                if string[i] in dict_of_roman and s1 >= s2:
                        integer += dict_of_roman[string[i]]
                        i += 1

                elif string[i] in dict_of_roman and s1<s2:
                    value = dict_of_roman[string[i+1]] - dict_of_roman[string[i]]
                    integer += value
                    i += 2
            else:
                integer += dict_of_roman[string[i]]
                i += 1
                print(integer)
roman_to_int('XLI')
roman_to_int('XXV')
roman_to_int('MMMDCX')