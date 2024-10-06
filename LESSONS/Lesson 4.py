 # Наданий масив чисел, треба знайти значення, що є подавлячою більшістю.
 # Майоритарний елемент — це елемент, який з'являється більше ніж ⌊n / 2⌋ разів. Ви можете припустити, що майоритарний елемент завжди існує в масиві.

 # Example 1:
 # Input: nums = [3,2,3]
 # Output: 3
 #
 # Example 2:
 # Input: nums = [2,2,1,1,1,2,2]
 # Output: 2


#------------------------------------
#РІШЕННЯ ЗА ДОПОМОГОЮ СОРТУВАННЯ
#Можна відсортувати масив, і взяти число посередині. так як наше шукане має к-сть більше за половину масива, серединка в будь-якому випадку буде репрезентцвати шукане
#Сортування + взяти середину

#------------------------------------
#РІШЕННЯ ЗА ДОПОМОТОЮ ПЕРЕБОРУ

def finder(nums):
    dic = {} #словник для ключа (число), значення (к-сть входжень)
    max = 0 #максимальне входження
    majorityNumber = 0 #число, яке максимально входить

    print(f"Переберемо всі елементи масиву {nums}")
    for el in nums:
        print("-"*20)
        print(f"Беремо число {el}")
        if el not in dic:
            print("Такого числа ще немає в словнику, додаємо його туди як ключ і даємо йому значення 1 (к-сть входжень).")
            dic[el] = 1
            print(dic)
        else:
            print("Таке число вже є словнику, додаємо йому до ключа значення 1 (к-сть входжень +1).")
            dic[el] += 1
            print(dic)

        if dic[el] > max:
            print(f"Оу, кількість входжени числа {el} = {dic[el]} і воно перевищило попередній максимум ({max})! Тож тепер чило {el} з к-стью входжень {dic[el]} є новим максимумом")
            max = dic[el]
            majorityNumber = el


    print(f"Ми пройшли увесь масив, максимальне входження число {majorityNumber} ({dic[majorityNumber]} разів)")
    return majorityNumber

nums = [2,2,1,1,1,2,2]
result = finder(nums)
print(result)


# рішення номер 2
nums = [2,2,1,1,1,2,2]
for el in nums:
    if nums.count(el) > len(nums)/2:
        print(el)
        break




#-------------------------------------------------------


 # Дано непорожній масив цілих чисел nums, де кожен елемент з'являється двічі, за винятком одного. Знайдіть це єдине число.
 # Ви повинні реалізувати розв'язок з лінійною складністю часу та використовувати тільки константний додатковий простір.
 #
 # Example 1:
 # Input: nums = [2,2,1]
 # Output: 1
 #
 # Example 2:
 # Input: nums = [4,1,2,1,2]
 # Output: 4
 #
 # Example 3:
 # Input: nums = [1]
 # Output: 1

nums = [4,1,2,1,2]
dic = {}

for x in nums:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for key in dic:
    if dic[key] == 1:
        print(key)


#------------------------------


# Сума тризначних паліндромів#
# Натуральне тризначне число називається паліндромом, якщо воно однаково читається зліва направо та справа наліво.
# Наприклад, тризначними паліндромами є числа: 202, 999, 727.
# Очевидно, що будь-яке натуральне тризначне число можна перетворити на тризначний паліндром, змінивши лише одну цифру,
# наприклад: 132→131 або 132→232.
# Розглянемо всі тризначні паліндроми, які можна отримати з заданого тризначного числа змінивши рівно одну цифру,
# тобто усі тризначні паліндроми, які відрізняються від заданого тризначного числа рівно в одному розряді.
# Напишіть програму, яка знайде суму усіх тризначних паліндромів, які можна отримати з заданого тризначного числа.

# Input
# Вашій програмі на вхід подається одне натуральне тризначне число.

# Output
# Виведіть одне число − суму всіх тризначних паліндромів, які відрізняються від заданого тризначного числа рівно в одному розряді.

# Examples

# Input #1
# 123
# Answer #1
# 444

# Input #2
# 120
# Answer #2
# 121

# Input #3
# 505
# Answer #3
# 4995

# --------------------------
# РІШЕННЯ ЗА ДОПОМОГОЮ МАСИВА З ЧИСЛАМИ

txt = input()
lst = []

for i in list(txt):
    lst.append(int(i)) #створюємо масив з числами

result = 0
if lst[0] == lst [2]: #варіант, якщо 1 і 3 числа однакові, наприклад 505, то результат буде 515+525+...+595
    for x in range(10):
        if lst[1] != x: #оригінальне число пропускаємо, не додаємо до суми, бо за умовою треба знайти суму паліндромів, без самого числа
            result = result + lst[0]*100 + x*10 + lst[2]
else:  # тепер міняємо місцями 1 і 3 , а потім 3 і 1 числа, щоб отримати поліндроми (123 -> 121, 323)
    result = result + lst[0]*100 + lst[1]*10 + lst[0] #підставляємо замість третього числа перше, наприклад 123 -> 121
    if lst[2] != 0: #якщо остання цифра числа 0, то паліндром з 0 не зробиш (120 не перетвориш на 020), тому числа з 0 в кінці пропускаємо
        result = result + lst[2] * 100 + lst[1] * 10 + lst[2]
print(result)

# --------------------------
# РІШЕННЯ ЗА ДОПОМОГОЮ ТЕКСТА

def change_char(txt, i, char): #функція міняє 1 індекс в тексті на заданний символ
    arr = list(txt)
    arr[i] = char
    new_string = ''.join(arr)
    return new_string

txt = input()

if txt[0] != txt[2]: #варіант, коли число не є саме поліндромом, тобто воно не є 505 або 434
    p1 = change_char(txt, 0, txt[2])  # робимо змінну з одним варіантом поліндрома
    p2 = change_char(txt, 2, txt[0])  # робимо змінну з іншим варіантом поліндрома

    if p1[0] == "0": # якшо перший символ 0 - то текстова строка міняється на 0
        p1 = "0"
    if p2[0] == "0": # якшо перший символ 0 - то текстова строка міняється на 0
        p2 = "0"

    sum = int(p1) + int(p2) #знаходимо суму

else: #варіант, коли число саме є поліндромом, тобто воно є 505 або 434
    sum = 0
    for i in range(10):
        if str(i) != txt[1]:
            p = change_char(txt, 1, str(i))
            sum += int(p)

print(sum)




