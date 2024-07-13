# // You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# // The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# // Increment the large integer by one and return the resulting array of digits.
#
# // Example 1:
# // Input: digits = [1,2,3]
# // Output: [1,2,4]
# // Explanation: The array represents the integer 123.
# // Incrementing by one gives 123 + 1 = 124.
# // Thus, the result should be [1,2,4].
#
# // Example 2:
# // Input: digits = [4,3,2,1]
# // Output: [4,3,2,2]
# // Explanation: The array represents the integer 4321.
# // Incrementing by one gives 4321 + 1 = 4322.
# // Thus, the result should be [4,3,2,2].
#
# // Example 3:
# // Input: digits = [9]
# // Output: [1,0]
# // Explanation: The array represents the integer 9.
# // Incrementing by one gives 9 + 1 = 10.
# // Thus, the result should be [1,0].


#ВАРІАНТ 1

#digits = [9,7,9]
digits = [9,9,9]
l = len(digits)

for i in range(l-1, -1, -1): #проходимо з останнього індексу до нульового по зменшенню
    print("Наш масив --> ", digits)
    print("Розглядаємо індекс ", i)
    if i == l-1:  #окремо розглядаємо останнє число, тут просто додаємо 1
        print(f"Це останній розряд. додаємо числу {digits[i]} одиницю")
        digits[i] += 1

    if digits[i] == 10: #якщо в поточному індексі стоїть число 10, то...
        print("В цьому розряді стоїть 10, треба робити перетворення. Записуємо туди 0 і робимо перевірку, чи існує більший розряд")
        digits[i] = 0 #міняємо його на 0
        if i==0:  #якщо цей розряд останній
            print("Це був останній розряд, тобто нам треба додати ще один розряд і вставити туди одиницю")
            digits.insert(0, 1) #Додаємо ще один розряд і чтавимо в нього одиницю
        else: #якщо цей розряд не останній
            print("Більший розряд існує, збільшуємо його на одиницю")
            digits[i - 1] += 1  # змінюємо наступний розряд на 1
    else:
        print("Збільшувати цей розряд не треба")
    print("Наш масив --> ", digits)
    print("-"*20)

print(digits)


#ВАРІАНТ 2

digits = [9,9,9]
string = str(digits)
num = int(string)
num += 1
string = str(num)
digits = list(digits)
for i in digits:
    digits[i] = int(digits[i])
print(digits)
