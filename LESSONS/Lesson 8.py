#Fibonacci

#Заняття потребує лекції про рекурсію

 # The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#  Числа Фібоначчі, що зазвичай позначаються F(n), формують послідовність, звану послідовністю Фібоначчі, так що кожне число є сумою двох попередніх, починаючи з 0 і 1. Тобто,
 # F(0) = 0, F(1) = 1
 # F(n) = F(n - 1) + F(n - 2), for n > 1.
 # Given n, calculate F(n).
 #
 # Example 1:
 # Input: n = 2
 # Output: 1
 # Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
 #
 # Example 2:
 # Input: n = 3
 # Output: 2
 # Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
 #
 # Example 3:
 # Input: n = 4
 # Output: 3
 # Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

def fib(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))

#-------------------------------------------
#Знаходження n-го числа фібоначі РЕКУРСИВНОЮ функцією

counter = 0 #лічильник, який виводить кількість викликів функції
def fib_rec(number):
    global counter
    counter += 1
    if number == 1 or number == 2:
        return 1
    else:
        return fib_rec(number-1) + fib_rec(number-2)
print(fib_rec(10))
# print(fib_rec(20))
# print(fib_rec(40))
print(counter)

#-------------------------------------------
#Знаходження n-го числа фібоначі РЕКУРСИВНОЮ функцією
def fib(num, n1, n2):
    print(n1 + n2)
    if (num - 1 >= 0):
        return fib(num - 1, n1 + n2, n1)

fib(10, 1, 1)

#-------------------------------------------
#Знаходження n-го числа фібоначі Лінійною функцією

def fib_lin(number, counter):
    fib1, fib2 = 1, 2
    number = number -2
    while number > 0:
        fib_next = fib1 + fib2
        fib1, fib2 = fib2, fib_next
        number -= 1
        counter += 1
    return fib2

counter = 0
print(fib_lin(10, counter))
print(counter)

#-------------------------------------------
#Знаходження n-го числа фібоначі Лінійною функцією за допомогою масива list
counter = 0
def fib_list(number):
    lst = [1,1]
    number -= 2
    while number > 0:
        number -= 1
        lst.append(lst[-1]+lst[-2])
        global counter
        counter +=1
    return(lst[-1])

print(fib_list(10))
print(counter)




#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------


# // Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# // Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#

# // Дано ціле 32-бітне ціле число зі знаком x, поверніть x з перевернутими цифрами. Якщо переворот x викликає вихід значення за межі діапазону 32-бітних цілих чисел [-2^31, 2^31 - 1], тоді поверніть 0.
# // Припустимо, що середовище не дозволяє вам зберігати 64-бітні цілі числа (підписані або беззнакові).
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



#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------


# // Given a string s consisting of words and spaces, return the length of the last word in the string.
# // A word is a maximal substring consisting of non-space characters only.
#
# // Example 1:
# // Input: s = "Hello World"
# // Output: 5
# // Explanation: The last word is "World" with length 5.
# //
# // Example 2:
# // Input: s = "   fly me   to   the moon  "
# // Output: 4
# // Explanation: The last word is "moon" with length 4.
# //
# // Example 3:
# // Input: s = "luffy is still joyboy"
# // Output: 6
# // Explanation: The last word is "joyboy" with length 6.


# // Дано рядок s, що складається зі слів та пробілів, поверніть довжину останнього слова в рядку.
# // Слово — це максимальний підрядок, що складається тільки з непробільних символів.
# // Приклад 1:
# // Вхідні дані: s = "Hello World"
# // Вихідні дані: 5
# // Пояснення: Останнє слово — "World", його довжина 5.
# //
# // Приклад 2:
# // Вхідні дані: s = " fly me to the moon "
# // Вихідні дані: 4
# // Пояснення: Останнє слово — "moon", його довжина 4.
# //
# // Приклад 3:
# // Вхідні дані: s = "luffy is still joyboy"
# // Вихідні дані: 6
# // Пояснення: Останнє слово — "joyboy", його довжина 6.

string = "luffy is still joyboy      "

#РІШЕННЯ 1
lst = string.split()
last_word = lst[len(lst)-1]
print(len(last_word))

#РІШЕННЯ 2
string = "luffy is still joyboy      "

counter = 0
for i in range(len(string)-1, -1, -1):
    if string[i] == " " and counter > 0:
        break
    elif string[i] != " ":
        counter += 1
print(counter)

