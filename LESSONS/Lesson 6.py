 # https://leetcode.com/problems/island-perimeter/description/
 # Вам дано масив, який представляє карту землі і суші, де grid[i][j] = 1 означає сушу, а grid[i][j] = 0 означає воду.
 # Клітинки сітки з'єднані горизонтально/вертикально (не по діагоналі). Сітка повністю оточена водою, і є рівно один острів
 # (тобто одна або більше з'єднаних клітинок суші).
 # Острів не має "озер", тобто вода всередині не з'єднана з водою навколо острова. Одна клітинка є квадратом зі стороною довжиною 1.
 # Сітка прямокутна, ширина та висота не перевищують 100. Визначте периметр острова.
 #
 # Example 1:
 # Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
 # Output: 16
 # Explanation: The perimeter is the 16 yellow stripes in the image above.
 #
 # Example 2:
 # Input: grid = [[1]]
 # Output: 4
 #
 # Example 3:
 # Input: grid = [[1,0]]
 # Output: 4

counter = 0 #ксть сторін периметру
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

width = len(grid[0]) #ширина таблиці
height = len(grid) #висота таблиці

for i in range(height): #перебираємо по висоті
    for j in range(width): #перебираємо по ширині
        if grid[i][j] == 0:  #якщо попали на воду, то йдемо далі
            continue

        # попали на землю
        if (j - 1) < 0 or  grid[i][j - 1] == 0: # Якщо зліва ячейка випадає за 0 індекс таблиці або якщо ліва ячейка - це вода
            counter += 1
        if (j + 1) >= width or grid[i][j + 1] == 0: # Якщо справа ячейка випадає за 0 індекс таблиці або якщо права ячейка - це вода
            counter += 1
        if (i - 1) < 0 or  grid[i-1][j] == 0: # Якщо верхня  ячейка випадає за 0 індекс таблиці або якщо нагорі ячейка - це вода
            counter += 1
        if (i + 1) >= height or grid[i + 1][j] == 0: # Якщо внизу ячейка випадає за 0 індекс таблиці або якщо нижня ячейка - це вода
            counter += 1

print(counter)


#------------------------------------------------------,


# Дано ціле число numRows, поверніть всі послідовності з трикутника Паскаля.
# У трикутнику Паскаля кожне число є сумою двох чисел безпосередньо над ним, як показано:
# https://drive.google.com/file/d/1d9SP8Zhqrfr6LXGH3QMv74zpzAvaIXIN/view?usp=sharing
# https://drive.google.com/file/d/1V-rZvk3_yiiQeRr3Nypkp9QewpzJz5E5/view?usp=sharing
# https://drive.google.com/file/d/1ppa478oX_Uz6E9oCCyR28MuKmfYpgB0u/view?usp=sharing

 # Example 1:
 # Input: numRows = 5
 # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 #
 # Example 2:
 # Input: numRows = 1
 # Output: [[1]]


numRows = 5
list = []
print(f"Створюємо масив для піраміди довжиною {numRows}")
for i in range(numRows):
    new_row = []
    print("-"*25)
    print(f"Створюємо рядок номер {i}")
    for j in range(i+1):
        if j == 0 or j == i:
            print("Ми на першому/крайньому елементі, тому ставимо одиницю")
            new_row.append(1)
        else:
            print(f"Дивимося суму двох елементів над нами ({list[i-1][j]} і {list[i-1][j-1]}), робимо їх суму, додаємо в піраміду")
            num = list[i-1][j] + list[i-1][j-1]
            new_row.append(num)
        input()

    print("Ми готові оновити піраміду новою строкою")
    list.append(new_row)

    lenght = len(list)
    for row_num in range(len(list)):
        spaces = lenght - row_num
        print(" " * spaces, end="")
        print(list[row_num])

