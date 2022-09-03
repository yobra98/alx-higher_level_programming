#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom_nums = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    result = 0
    for j in range(len(roman_string)):
        if j > 0 and rom_nums[roman_string[j]] > rom_nums[roman_string[j - 1]]:
            result += rom_nums[roman_string[j]] - 2 * \
                        rom_nums[roman_string[j - 1]]
        else:
            result += rom_nums[roman_string[j]]
    return result
