# ----------------------------------------

# В Анатолія є A яблук та B груш, а в Бориса C яблук та D груш.
# Вони хочуть роздати яблука та груші N дітям. Кожна дитина хоче X яблук та Y груш.
# Визначте, чи зможе Анатолій та Борис роздати яблука та груші дітям так, щоб кожен отримав те, що він хоче.

# Input
# Перший рядок містить сім цілих чисел a, b, c, d, n, x, y (1≤a,b,c,d,n,x,y≤100).

# Output
# Виведіть «Yes», якщо хлопці зможуть це зробити, або «No» — інакше.
# Ви можете виводити букви у будь-якому регістрі.

# Examples
# Input
# 3 4 5 4 3 1 2
# Answer
# Yes

a, b, c, d, n, x, y = input().split()
a= int(a)
b= int(b)
c= int(c)
d= int(d)
n= int(n)
x= int(x)
y= int(y)

apples = a + c
pears = b + d

if apples/n >= x and pears / n >= y:
    print("YES")
else:
    print("NO")


# ----------------------------------------


#ПОВТОР ТЕМИ "ДІЇ З СТРОКАМИ"

x = '1234567890'
x = "Тут буде якась строка"
x = '''
З використанням трьох одинарних кавичок
ми можемо записувати абзац.
'''
print("-------------------------------")

# Пошук в строці
print('a' in x) #Пошук символа в строці
print('0' in x)
print('456' in x) #Пошук підстроки в строці
print('654' in x)

print("-------------------------------")

# кількість входжень в строку

x = '123456789012345678901234567890'

print(x.count('2')) # Кількість входження символа 2 в строку х
print(x.count('23')) # Кількість входження підстроки 23 в строку х
print('123456789012345678901234567890'.count('23'))

print("-------------------------------")

# upper() and lower()
x = 'asdfghj1'
x = x.upper() # Переводимо всі символи строки в Upper Case
print(x)
x = x.lower() # Переводимо всі символи строки в Lower Case
print(x)

word = input("Напиши слово на букву Ч - ")
word = word.lower()

if word.startswith("ч"):
    print("YES")
else:
    print("No")

print("-------------------------------")

# replace(a,b) - заміна частини строки іншою строкою
x = '123456789045'
print(x)

res = x.replace('45', '+=+') # в строці х заміняємо всі входження "45" на "+=+"
print(res)

res = x.replace('32', '+=+')
print(res)

print("-------------------------------")

# Перевірка, чи стартує строка з вказаних символів. Повертає True або False
tpl = '123456'
print(tpl.startswith('123')) # Перевірка, чи починається строка tpl з символів "123"
print(tpl.startswith('321'))
print(tpl.endswith('56'))
print(tpl.endswith('65'))

print("-------------------------------")

# Пошук індекса (місця) символа в строці. Індексація починається з 0
tpl = 'asdfghjkl'
print(tpl.find('a')) # Повертає індекс букви "а" в строці tpl
print(tpl.find('f'))
print(tpl.find('df')) # Повертає індекс букви "d" в строці tpl
print(tpl.find('1'))

print('-'*100)
x = '0123456789'
tpl = 'asdfghjkl'
print(x)
print(x[0])
print(x[6])
print(tpl[0])
print(tpl[6])

# print(x[100])
print(x[-1])
# print(x[-20])

print("------------------------------")

text = "xxx5xxx" #Використання однакових індексів з різними знаками не видасть однакове положення навіть в симетричних строках
print(text[3])
print(text[-3])

print("------------------------------")

print(x[2:5]) # Виведе всі букви з 2 по 4 індекс
print(x[2:5].find('3')) # Перевірить, чи є символ "3" в обрізацій строці. Поверне True/False

print(x[2:]) # Виведе всі букви, починаючи з індексу 2
print(x[:5]) # Виведе всі букви з початку аж до індекса 4

print(x[-3:]) # Виведе всі букви, починаючи з індексу -3 і до кінця слова
print(x[-5:-3]) # Виведе всі букви, починаючи -5 і закінчуючи -4 індексом
print(x[6:3])

print('-'*100)
x = '0123456789'
print(x[2:8])
print(x[2:8:1]) # Вивід кожної букви в підстроці
print(x[2:8:2]) # Вивід кожної другої букви в підстроці
print('--->', x[2:8:-1]) # Вивід букв задом наперед в підстроці
print(x[::-1]) # Вивід всього слова задом наперед

a = 1
b = 5
print(x[a:b:b//3])

print('-'*100)

# split - розділення строки на частини

x = 'as df gdd 111 34 66 77'
print(x.split()) # Якщо нічого не вказати в (), то розділення пройде по пробілам
print(x.split(' ')) # Розділення по пробілам

y = x.split()
print(type(y)) # Розділення тексту формує тип даних масив список (LIST)

x = 'as12df12gdd12111123412661277'
print(x.split('12')) # Розділення по тексту "12"

x = '''as12df12gdd121 11123412661277
qwert   sdfghj'''
print('--->', x.split()) #Розділення абзацу

print('----------------------------------------')

#Довжина рядка
s = "asfsgrthty'hgvjfhsvnjvb"
print(len(s))

print('----------------------------------------')

# for for string

s = 'qwertyuio'

for i in s:
    print('--->', i)

print('----------------------------------------')

#Конкатенація
string = "this" + "is" + "text"
print(string)

string2 = ""
for i in string:
    string2 += i
    print(string2)

# перевірка на регистр
x = "AA"
print(x.isupper())
print(x.islower())

x = "Aa"
print(x.isupper())
print(x.islower())



# ----------------------------------------



# Степан вдало пройшов співбесіду і ось уже як чотири місяці працює на одній із самих престижних ІТ компаній.
# Прийшов час здавати проект менеджеру і Степан, як істинний студент, все виконує у останню ніч перед здачею.
# Набирає текст Степан звичайно дуже швидко, але неуважно.
# От і цього разу останню частину тексту він набрав не звернувши уваги, що випадково натиснув клавішу caps lock.
# Таким чином великі букви були набрані маленькими, а маленькі великими. Інші символи він набрав вірно.
# Степан настільки стомився, що немає сил виправити помилки, і він вирішив кілька годин поспати.
# Допоможіть Степану, доки він спить, напишіть програму, яка виправляє неуважно набраний текст.
# Формат вхідних даних: перший рядок вхідного файлу містить неуважно набраний Степаном текст, який містить не більше 500 символів.
# Формат вихідних даних: вихідний файл має містити виправлений текст.
#
# Приклад вхідних і вихідних даних:
# sCHOOL
# School

text = input()

res = ""
for s in text:
    if s.islower():
        res += s.upper()
    else:
        res += s.lower()

print(res)



# ----------------------------------------


# Журі олімпіади з інформатики прийняло рішення, що всі учасники мають отримати сертифікат:
# - ті, хто набере не менш ніж 90% від максимальної кількості балів, отримають сертифікат OUTSTANDING − видатний результат;
# - ті, хто набере менше ніж 90%, але не менш ніж 74% від максимальної кількості балів, отримають сертифікат EXCELLENT − відмінний результат;
# - ті, хто набере менше ніж 74%, але не менш ніж 60% від максимальної кількості балів, отримають сертифікат VERY GOOD − дуже  добрий результат;
# - усі інші отримають сертифікат PARTICIPANT.
# Нам потрібна програма, для автоматизації вирішення, який сертифікат має отримати учасник олімпіади. Напишіть таку програму!

# Input
# У першому рядку вхідних даних записано натуральне число M − максимальний бал, який можна отримати на олімпіаді.
# У другому рядку записано дійсне число K − кількість балів учасника олімпіади.
# Гарантується, що 1≤M≤1000 та 0.0≤K≤M, число K подається не більш ніж з однією цифрою після крапки.
# OutputВиведіть назву сертифіката, який має отримати учасник олімпіади.

# Examples

# Input #1
# 100
# 100
# Answer #1
# OUTSTANDING

# Input #2
# 1000
# 850.5
# Answer #3
# EXCELLENT

# Input #4
# 1000
# 700.1
# Answer #4
# VERY GOOD

# Input #5
# 1000
# 599.9
# Answer #5
# PARTICIPANT


M = float(input())
K = float(input())

result = K / M

if result >= 0.9:
    print("OUTSTANDING")
elif result >= 0.74:
    print("EXCELLENT")
elif result >= 0.6:
    print("VERY GOOD")
else:
    print("PARTICIPANT")



# ----------------------------------------


# Вам дано рядок jewels, що представляють типи каменів, які є коштовностями, і рядок stones, що представляє камені, які ви маєте.
# Кожен символ у рядку stones є типом каменю, який ви маєте. Ви хочете дізнатися, скільки з ваших каменів також є коштовностями.
# Літери чутливі до регістру, тому "a" вважається іншим типом каменю, ніж "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0


jewels = "aA"
numJewelsInStones = 0
stones = "aAAbbbb"

counter = 0
for i in stones:
    if i in jewels:
        counter += 1

print(counter)
