# Перевод римьских чисел в звичайні і навпаки

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



def int_to_roman(num):
    print("Int to Romanian")
    num_map = {
        1: "I", #однобуквені
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",

        4: "IV", #двобуквені
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM",

    }
    result = ""
    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]: # перебираємо числа від більшого до меньшого в рамках заданого діапазона
        # If n in list then add the roman value to result variable
        while n <= num: #зменьшуємо основне число поки воно не стане меньше за n
            result += num_map[n]  # додаємо букву (вибірка з словника по ключу) до строки
            num -= n # зменьшуємо основне число на значення букви, яку вже додали до строки
    return result


def roman_to_int(roman):
    print("Romanian to int")
    num_map = {
        "I": 1,  # однобуквені
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,

        "IV": 4,  # двобуквені
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900

    }
    result = 0

    i = 0
    while i < len(roman): # проходимось по індексам букв
        if i+1 < len(roman) and roman[i:i+2] in num_map: # якщо є можливість розглянути пару букв і ця пара є в двобуквених сполуках
                result += num_map[roman[i:i+2]] # до результату додається число, що відповідає двобуквеній сполуці
                i+=2 # індекс перепригує на 2 пункту, бо ми використали двобуквену сполуку.
        else:
            result += num_map[roman[i]]  # до результату додається число, що відповідає однобуквеній сполуці
            i+=1

    return result



num = input("Що конвертуємо? - ")
try:
    num = int(num) # якщо у нас число, то переводимо в символи
    result = int_to_roman(num)
except:
    result = roman_to_int(num) "Якщо у нас символи, то переводимо в число"
print("res = ", result)