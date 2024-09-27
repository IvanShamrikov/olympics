# Конфетна проблема Степана

# Степан закохався і вирішив привернути уваги дівчини великою коробкою цукерок.
# За порадою друзів він поїхав на саму відому кондитерську фабрику ShenRo і дізнався, що великі коробки цукерок мають трикутну форму.
# Цукерки в цих коробках розташовуються у кілька рядів.
# У першому ряду знаходиться одна цукерка, у другому – дві, у третьому – три цукерки і так далі.
# На фабриці випускаються коробки цукерок з любим числом рядів у межах від 1 до N.
# Степан хоче купити одну із таких коробок.
# Але є одна проблема: його дівчина засмутиться, якщо кількість цукерок у коробці не буде ділитись націло на M,
# тому що у цьому випадку комусь із друзів дівчини дістанеться більше цукерок, чим іншим, або ж якісь цукерки залишаться лишніми.
# Тому Степан вирішив, що число цукерок у коробці має обов’язково ділитись націло на M.
# При виборі подарунка Степан зіткнувся з проблемою придбання відповідної коробки цукерок,
# оскільки можливих варіантів вибору коробки цукерок виявилося надто багато. Не довго думаючи,
# Степан вирішив звернутись за допомогою до учасників олімпіади.
# Вам необхідно по заданих числах N і M знайти число способів вибору коробки цукерок із множини коробок з кількістю рядів від 1 до N.
# Способи вважаються різними, якщо їм відповідають коробки з різною кількістю рядів цукерок.

# Формат вхідних даних: перший рядок вхідного файлу містить два цілих числа N - максимальна кількість рядів цукерок у
# коробці і M – кількість друзів дівчини Степана (1 ≤ N, M ≤ 2*109) відповідно.
# Формат вихідних даних: вихідний файл має містити одне ціле число - кількість різних способів вибору коробки цукерок.

# Приклад вхідних та вихідних даних:
# problem.in - 20 10
# problem.out - 4

# problem.in - 53 199
# problem.out - 0

# problem.in - 5705 145
# problem.out - 157


rows = 20
friends = 10
res = 0

for i in range(rows):
    #знаходимо суму ряду арифметичної прогресії (кількість цукерок) для кожного варіанту розміру коробки
    var = (1 + i) * i / 2
    #якщо ділиться без остачі на кількість друзів, то коробка підходить
    if var % friends == 0:
        res += 1

print(res)


# ----------------------------------------

#Види масивів

#list
lst = []
lst = list()
print(lst)
print(type(lst))
lst = [1, 2.2, 3, 4, "text", None, True, ["a", "b", "c"]]

#tuple
tpl = ()
tpl = tuple()
print(tpl)
print(type(tpl))
tpl = tpl = (1, 2.2, "test", None, True, False, [], ("x", "y", "z"))

#set
st = set()
st = {1, 2.2, "test", None, True, False, [], ("x", "y", "z")}
print(st)
print(type(st))

# FrozenSet
fst = frozenset()

# DICTIONARY

dct = dict()
dict = {"key 1" : "value 1",
        "key 2" : "value 2",
        "key 3" : "value 3",
        "key 4" : "value 4",}


dict = {1 : "value int",
        2.23 : "value float"
        }
print(dict)
print(dict[1]) # Виводимо значення по ключу
print(dict.keys()) # Виводимо list ключів
print(dict.values()) # Виводимо list значень


# ----------------------------------------


# Арифметика

# Молодший брат Степана Мишко навчається у першому класі.
# Він дуже допитливий і постійно дістає Степана запитаннями: А скільки? А чому?
# Сьогоднішній день не виключення.
# Мишко  каліграфічно виписує цифри в ряд і запитує: А скільки різних цифр у записі цього числа.
# На перші приклади Степан швидко знаходив відповідь.
# Але Мишко чим далі, тим більші числа записував.
# Це стало для Степана проблемою.

# Допоможіть Степану, напишіть програму, яка визначає, кількість різних цифр у числі Мишка.
# Формат вхідних даних: перший рядок вхідного файлу містить одне ціле число N(1 ≤ N ≤ 10^1000), записане Мишком.
# Формат вихідних даних: вихідний файл має містити одне число – кількість різних цифр у числі.
#
# Приклад вхідних і вихідних даних:
# count.in - 1233
# count.out - 3

# ---
# перший варіант

x = input()
y = set(x) #використовуємо масив типу set(кучу), який зберігає тільки унікальні значення
print(len(y))

# ---
# другий варіант

x = list(input())

res = []
for i in x:
    if i not in res:
        res.append(i)

print(len(res))



# ----------------------------------------



# Ігорчик та яблучка

# В Ігорчика є сад з трьома видами яблук: зелених, жовтих та червоних.
# Цього року він зібрав n зелених, m жовтих та k червоних яблук.
# Оскільки Ігорчик дружить з усіма сусідами, то він вирішив роздати яблука, які зібрав. Він знає, що кожен сусід буде задоволений,
# якщо Ігорчик подарує йому яблука принаймні двох різних видів.
# Допоможіть Ігорчику знайти максимальну кількість сусідів, які можуть бути задоволені.

# Input
# Перший рядок містить три цілі числа n, m та k (0≤n,m,k≤100) — кількість зелених, жовтих та червоних яблук відповідно.

# Output
# Виведіть одне ціле число — відповідь на задачу.

# Examples

# Input
# 6 3 4
# Answer
# 6

n = 6
m = 3
k = 4
neighbors = 0

while n > 0:  #поки зелених яблук більше0, пари робляться зелене-жовте, зелене-червоне
    if m > 0:
        n -= 1
        m -= 1
        neighbors += 1

    if n > 0 and k > 0:
        n -= 1
        k -= 1
        neighbors += 1

#тут зелені яблука закінчились. Можна подивитись, скільки пар можна зробити з жовтих і червоних

# while m>0  and  k>0 : # варіант кінцівки номер 1
#     m -= 1
#     k -= 1
#     neighbors += 1

neighbors += min(m, k) # варіант кінцівки номер 2

print(neighbors)



# ----------------------------------------


# Є робот, який починає рухатися з позиції (0, 0), тобто з початку координат на площині. Дано послідовність його рухів.
# Необхідно визначити, чи опиниться робот у початковій точці (0, 0) після завершення всіх своїх рухів.
# Вам надано рядок moves, який представляє послідовність рухів робота, де moves[i] представляє його i-й рух.
# Допустимі рухи: 'R' (праворуч), 'L' (ліворуч), 'U' (вгору) та 'D' (вниз).
# Поверніть True, якщо робот повернеться до початкової точки після завершення всіх рухів, інакше False.
# Примітка: Напрямок, в якому "дивиться" робот, не має значення. 'R' завжди переміщує робота на одну клітинку праворуч,
# 'L' завжди переміщує його ліворуч і т.д. Також вважається, що всі рухи мають однакову величину.

# Приклад 1:
# Вхід: moves = "UD"
# Вихід: True
# Пояснення: Робот рухається один раз вгору, а потім один раз вниз. Усі рухи мають однакову величину,
# тому він повернувся до початкової точки, звідки почав. Тому повертаємо True.

# Приклад 2:
# Вхід: moves = "LL"
# Вихід: False
# Пояснення: Робот рухається двічі ліворуч. Він опиняється на дві "клітинки" лівіше від початкової точки.
# Повертаємо False, оскільки він не знаходиться у початковій точці після завершення рухів.

moves = "UD"
x = 0
y = 0

movesInCords = {
        "U": { "x": 0, "y": 1 },
        "D": { "x": 0, "y": -1 },
        "L": { "x": -1, "y": 0 },
        "R": { "x": 1, "y": 0 }
}

for i in moves:
    x += movesInCords[i]["x"]
    y += movesInCords[i]["y"]

if x == 0 and  y == 0:
    print(True)
else:
    print(False)