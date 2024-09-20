 # Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
 # The returned integer should be non-negative as well.
 # You must not use any built-in exponent function or operator.
 # For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 #
 # Example 1:
 # Input: x = 4
 # Output: 2
 # Explanation: The square root of 4 is 2, so we return 2.
 #
 # Example 2:
 # Input: x = 8
 # Output: 2
 # Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned


 #ПЕРЕД ЗАНЯТТЯМ ЗРОБИТИ ЛЕКЦІЮ З БІНАРНОГО ПОШУКУ


# ВАРІАНТ 1
x = 1000000
flag_left = x
iter = 0 #к-сть операцій в програмі

while True:
    if flag_left * flag_left < x: #якшо число в квадраті меньше нашого початкового, то ми знайшли нижній поріг
        break
    flag_left = flag_left//2 #ділимо число на 2
    iter += 1

flag_right = flag_left
while True:
    if flag_right * flag_right > x: #якшо число в квадраті більше нашого ісходного, то ми перейшли верхній поріг
        break
    flag_right = flag_right + 1
    iter += 1
print(flag_right-1) #попереднє число перед переходом верхнього порогу і буде відповідь задачі
print(iter) #к-сть операцій в програмі


# ВАРІАНТ 2

x = 37
flag_left = 0
flag_right = x
iter = 0

while flag_left < flag_right:
    print(f"Лівий флажок = {flag_left}, Правий флажок = {flag_right}")
    middle = ( flag_right + flag_left ) // 2 #Знаходимо серединку між флагами по модулю
    print(f"Знаходимо середину між флагами. Середнє значення = {middle}")

    if middle * middle > x :
        print(f"Квадрат середнього значення {middle} ({middle*middle}) більший за начальне число {x}.")
        flag_right = middle - 1
        print(f"Віднімаємо від середнього значення одиницю і це число ({flag_right}) стає правим флажком.")

    elif middle * middle < x :
        print(f"Квадрат середнього значення {middle} ({middle*middle}) меньший за начальне число {x}.")
        flag_left = middle + 1
        print(f"Додаємо до середнього значення одиницю і це число ({flag_left}) стає лівим флажком.")

    iter += 1
    print(f"-"*25)

print(f"Лівий флажок ({flag_left}) перестав бути меньшим за правий флажок ({flag_right}). Отже, попереднє значення лівого флажка було вірним")
print(f"Відповідь = {flag_left-1}, кількість операцій = {iter}")