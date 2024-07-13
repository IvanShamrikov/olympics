# // The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# //(you may want to display this pattern in a fixed font for better legibility)
#
# // P   A   H   N
# // A P L S I I G
# // Y   I   R
# // And then read line by line: "PAHNAPLSIIGYIR"
#
# // Write the code that will take a string and make this conversion given a number of rows:
#
# // string convert(string s, int numRows);
#
# // Example 1:
# // Input: s = "PAYPALISHIRING", numRows = 3
# // Output: "PAHNAPLSIIGYIR"
#
# // Example 2:
# // Input: s = "PAYPALISHIRING", numRows = 4
# // Output: "PINALSIGYAHRPI"
# // Explanation:
# // P     I    N
# // A   L S  I G
# // Y A   H R
# // P     I

#Перед тим, як давати цю задачу, треба дати просту задачу на залишок від ділення.
#Наприклад, треба розподілити масив чисел з 1 до 48 по трьох корзинах послідовно
# На вході
# [1,2,3,4,5,...,48]
# на виході
# [1,4, ...]
# [2,5, ...]
# [3,6, ...]


s = "PAYPALISHIRING"
numRows = 4
lst = []

for i in range(numRows):
    lst.append([])
print(lst)

counter = 0
while len(s) > 0:
    if counter % (numRows-1) == 0: #спрацює для кожного третього стовпчика, починаючи з нуля
        for i in range(numRows): #записуємо літери в всі підмасиви по черзі
            if len(s) == 0: #numRows - це константа, тобто цикл for буде робитися фіксовану кількість разів.
                break       # Але ми при кожному спрацьовуванні обрізаємо строку.
                            # І може так статись, що в середині циклу строка закінчиться.
                            # Таким чином ми робимо перевірку довжини строки і припиняємо цикл якщо строка закінчилась


            lst[i] += s[0] #записуємо літеру в всі підмасиви по черзі
            s = s[1:] #видаляємо літеру, яку вже використали
            print(s)
            print("1 -->", lst)

    else: #спрацьовує в інших випадках
        lst[numRows-1 - (counter%(numRows-1))] += s[0] # numRows-1 - це загальна к-сть наших підмасивів
                                                    # counter%(numRows-1) - необхідність через циклічність масиву, розуміння цього повинно було прийти під час вирішення підготовчого завдання
        s = s[1:]   #обрізаємо сторку
        print(s)
        print("2 -->", lst)


    counter += 1 # переходимо до наступного стовпчика

