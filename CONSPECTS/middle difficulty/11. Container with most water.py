# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
#
#
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#
# Example 2:
# Input: height = [1,1]
# Output: 1

#ВАРІАНТ 1, не ефективний

lst = [1,8,6,2,5,4,8,3,7]
def calc(m, n, index_m, index_n): #Обчислюємо площу басейну, маючи висоти m,n та індекси між ними (ширина)
    print(f"У нас висоти бортів басейну {m} та {n} (з якиз беремо мінімальну, бо вода буде виливатись), а також ширина басейну як різниця індексів {index_m}, {index_n}")
    heigh = min(m, n)
    lenght = index_n - index_m
    sqr = heigh * lenght
    print(f"Площа = {sqr}")
    return sqr

iter = 0 #к-сть ітерацій
sqr_max = 0 #максимальна площа басейну.
for index_m in range(len(lst)): #вкладений цикл, який кожний борт порівнює з усіма наступними після нього.
    for index_n in range(index_m+1, len(lst)): #вкладений цикл, який кожний борт порівнює з усіма наступними після нього.
        print(f"Розглядаємо борт за індексом {index_m}({lst[index_m]}метрів) та борт {index_n}({lst[index_n]}метрів)")
        sqr = calc(lst[index_m], lst[index_n], index_m, index_n)
        if sqr > sqr_max:
            print(f"Ця площа {sqr} кв.м більша за попередню максимальну {sqr_max} кв.м. Зберігаємо її як максимальну")
            sqr_max = sqr

        else:
            print(f"Ця площа {sqr} кв.м меньша за попередню максимальну {sqr_max} кв.м. Тож максимум не змінюється")
        iter += 1
        print("-"*10)
    print("-"*25)

print(f"Ми закінчили перебір всіх бортів по черзі, максимальна площа = {sqr_max} кв.м")
print(iter)


#ВАРІАНТ 2,  ефективний

length = len(lst)  #довжина масива
left = 0 #індекс самого лівого борта
right = length-1 #індекс самого правого борта
max_sqr = 0
iter = 0

while left < right: #поки лівий борт не перейшов за правий
    width = right - left  #ширина контейнера (різність індексів)
    height = min(lst[left], lst[right]) #висота - меньший з бортів
    sqr = width * height #площа

    if sqr > sqr_max:
        print(f"Ця площа {sqr} кв.м більша за попередню максимальну {sqr_max} кв.м. Зберігаємо її як максимальну")
        sqr_max = sqr
    else:
        print(f"Ця площа {sqr} кв.м меньша за попередню максимальну {sqr_max} кв.м. Тож максимум не змінюється")

    # берем наступний борт зі сторони меньшого борта.
    if lst[left] < lst[right]:
        while left < right and lst[left] <= height: #доки новий борт меньший за поточний правий, то перебираємо ліві борти далі
            left += 1
            iter += 1
    else:
        while left < right and lst[right] <= height: #доки правий борт меньший за поточний лівий, то перебираємо праві борти далі
            right -= 1
            iter += 1



print(max_sqr)
print(iter)

