# // Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# // Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# // Example 1:
# // Input: x = 123
# // Output: 321
#
# // Example 2:
# // Input: x = -123
# // Output: -321
#
# // Example 3:
# // Input: x = 120
# // Output: 21
#
#
#
#
# --- РІШЕННЯ У ВИГЛЯДІ ТЕКСТОВОГО ПЕРЕБОРУ

# x = -321
#
# if x<0:
#     znak = -1
# else:
#     znak = 1
#
#
#
# y = str(abs(x))
# res = ""
#
# print(y)
# print(type(y))
# print(len(y))
# l = len(y)
#
#
# for i in range(l):
#     print(y[l-1-i])
#     res = res + y[len(y)-1-i]
#
# res = int(res)
#
# print(res * znak)



# --- РІШЕННЯ У ВИГЛЯДІ МАНІПУЛЯЦІЇ З ЧИСЛАМИ

x = -321
res = 0

znak = x / abs(x) #зберігаємо знак
x = abs(x) #зберігаємо число без знаку
lenght = len(str(abs(x))) #визначаємо довжину числа

for i in range(lenght): #перебираємо розряди по довжині числа
    z = x / (10**i) #ділимо число на 1, 10, 100, 1000 і т.д, кожен раз залишається все більший хвостик
    print("z --> ", z)
    z = round(z, 0) #округлюємо число до одиниць, таким чином остання цифра буде поточним числом на додавання до результату
    print("z --> ", z)
    res += (z % 10) * (10**(lenght-1-i)) #відокремлюємо останнє число і підносимо його в правильну степінь
    print("res --> ", res)

res = res * znak #додаємо знак
print(res)

