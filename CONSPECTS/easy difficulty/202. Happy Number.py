# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Example 2:
# Input: n = 2
# Output: false

#ПЕРЕД СТАРТОМ ЗАДАЧІ ТРЕБА ПРОГОВОРИТИ, ЩО ЧИСЛО БУДЕ ЩАСЛИВИМ, ЯКЩО НА ЯКОМУСЬ ЕПАТІ ВОНО ПЕРЕТВОРИТЬСЯ НА 1 АБО 7.
#БО ТІЛЬКИ ЦІ ЦИФРИ В КІНЦІ КІНЦІВ МОЖУТЬ СТАТИ ЩАСЛИВИМИ

n = 7
print("Початкове число =", n)

while True:
    print("-"*25)
    n = str(n)
    lst = list(n)
    n = 0
    print(f"Маємо такі числа -> {lst}")
    for i in range(len(lst)):
        lst[i] = int(lst[i])
        n = n + lst[i]**2
    print(f"Сума квадратів чисел = {n}")

    if n < 10:
        print(f"Сума квадратів чисел меньше 10.")
        if n == 7:
            continue
        if n == 1:
            print(f"Це число 1. Тобто початкове число було щасливим.")
            print(True)
        else:
            print(f"Це число не дорівнює 1. Тобто початкове число не було щасливим.")
            print(False)
        break