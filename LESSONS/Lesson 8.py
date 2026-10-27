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






#----------------------------------------
# https://uoi.eolymp.space/problems/544
# Копії без оригіналів
#
# Є n карток, пронумерованих від 1 до n.
# Спочатку кожна картка була порожньою або містила одне додатне ціле число.
# Однакові числа могли бути записані на кількох картках. Початковий вміст карток невідомий.
# З картками виконали m операцій копіювання. Під час операції (x,y) вміст картки y замінювали вмістом картки x.
# Вміст картки x при цьому не змінювався. Якщо картка x була порожньою, картка y також ставала порожньою.
# Вам відомі всі операції в порядку їх виконання. Також відомо, що після всіх операцій на картці i записане число ai.
# Отже, наприкінці всі картки непорожні.
#
# Визначте найменшу можливу кількість карток, на яких спочатку були записані числа.
# Якщо отримати заданий кінцевий вміст карток неможливо, повідомте про це.
#
# https://drive.google.com/file/d/1Mh7d5CtDKrj8wzcf5v2r3i7Ee7utZLuj/view?usp=sharing
# Приклад для n=3 та m=2
#
# Вхідні дані
# Перший рядок містить два цілі числа n та m (1≤n≤2⋅10**5, 0≤m≤2⋅10**5) — кількість карток і кількість операцій відповідно.
# Другий рядок містить n цілих чисел a1,a2,…,an(1≤ai≤10**9) — числа на картках після виконання всіх операцій.
# Кожен із наступних m рядків містить два цілі числа x та y (1≤x,y≤n, n<=y), які задають копіювання з картки x на картку y.
# Операції наведено в порядку їх виконання.
#
# Вихідні дані
# Виведіть одне ціле число — найменшу можливу кількість непорожніх карток на початку. Якщо отримати заданий кінцевий вміст
# карток неможливо, виведіть −1.

#
# Приклад 1
# Вхідні дані
# 3 2
# 2 1 2
# 1 2
# 3 1
# Вихідні дані
# 2
#
# Приклад 2
# Вхідні дані
# 2 1
# 1 2
# 1 2
# Вихідні дані
# -1
#
# Приклад 3
# Вхідні дані
# 4 3
# 7 7 7 7
# 1 2
# 2 3
# 3 4
# Вихідні дані
# 1

n,m = map(int, input().split())
value_result = list(map(int, input().split()))
moves = []

for i in range(m):
    x,y = map(int, input().split())
    moves.append([x,y])


position_result = []
for i in range(n):
    position_result.append("p"+str(i+1))

print(f"Кількість цифр = {n}")
print(f"Початкові позиції = {position_result}")
print(f"Рухи = {moves}")
print(f"Фінальні позиції - ???")

for i in range(len(moves)):
    print("-" * 20)
    move = moves[i]
    pos_from = move[0]-1
    pos_to = move[1]-1
    print(f"Рух номер {i+1}: {moves[i]}")
    print(f"Копіюємо з ячейки {pos_from+1}(маркер {position_result[pos_from]}) до ячейки {pos_to+1} (маркер {position_result[pos_to]})")
    position_result[pos_to] = position_result[pos_from]
    print(f"Поточні позиції: {position_result}")

print("-" * 30)
print(f"Фінальний масив позицій = {position_result}. Показує нам, які початкові позиції залишились в фіналі")
print(f"Фінальний масив чисел (заданий в умовах) = {value_result}")
print("-" * 20)
print("Тепер перевіримо, чи відповідають ці два масиви один одному. Зробимо бібліотеку, наповнимо унікальними елементами, а дублі будемо звіряти з наявними")

lib = {}
for i in range(n):
    pos = position_result[i]
    value = value_result[i]
    print()
    print("*"*20)
    print(f"Беремо пару з обох масивів: Позиція {pos} і значення {value}")
    if pos not in lib.keys():
        lib[pos] = value
        print(f"Такої позиції ще не додавалось в бібліотеку. Додамо позицію {pos} як ключ і до нього значення {value}")
        print(f"Бібліотека приймає вигляд {lib}")
    else:
        print(
            f"Бачимо, що в бібліотеці вже була така позиція {pos}, порівнюємо поточне значення {value} з тим, що вже лежить в бібліотеці по данній позиції (там лежить {lib[pos]})")
        if lib[pos] != value:
            print(f"От халепа! значення не збігається, тобто в фінальному переліку значень по умові задачі ({value_result}) стоять не ті ціфри, які мають!")
            print("Це явно помилка умови, тому виводимо відповідь -1")
            answer = -1
        else:
            print("Значення збігається, все добре")

    answer = len(lib.keys())

print()
if answer != -1:
    print(f"Ми закінчили перевірку відповідностей масивів Фінальних позицій і Фінальних значень. Помилок не знайдено")
    print(f"Відповіддю буде кількість ключів в бібліотеці {lib.keys()}. Тому що саме ці ключі дійшли до кінця і гарантовано мали б бути числами на самому початку")

print("Відповідь:",answer)