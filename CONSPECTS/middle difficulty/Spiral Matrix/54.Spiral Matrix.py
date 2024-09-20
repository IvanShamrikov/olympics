# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

rows = len(matrix)
cols = len(matrix[0])

x, y = 0, 0 #координати ячейки
dx, dy = 1, 0 #напрямок руху по х та у
res = [] #результат

for i in range(rows * cols): #к-сть кроків в матриці (к-сть комірок)
    res.append(matrix[y][x])
    matrix[y][x] = "." #заміняємо значення комірки на ".", щоб надалі ідентифікувати кінець строки або стовпця

    if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".": #якшо наступна ячейка випадає з границі по х/y, або вже була пройдена і там стоїть "."
        dx, dy = -dy, dx #хитро*опа схема зміни напрямку, пояснення нижче
        #dx = 1, 0, -1, 0, #нове коло# 1
        #dy = 0, 1, 0, -1, #нове коло# 0

    x += dx #зміна комірки на наступну відповідно до напрямку
    y += dy #зміна комірки на наступну відповідно до напрямку

print(res)



#-----------------------------------------------------
#Другий варіант

matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)
m = len(matrix[0])
cells = n * m

step_counter = 0
arr = [] #результат
offset = 0 #скільки ячеєк від краю треба не доходити. Або скільки ячеєк з того чи іншого краю вже пройдено
x = 0
y = 0
while step_counter < cells:
    print(f"Починаю нове коло з координат ({x},{y})")
    print("\nЙду направо")
    while x < m - offset and step_counter < cells:
        arr.append(matrix[y][x])
        print(f"Беру число {matrix[y][x]}, додаю до результату, маю {arr}")
        x+=1
        step_counter+=1

    x-=1
    y+=1

    print("\nЙду вниз")
    while y < n - offset and  step_counter < cells:
        arr.append(matrix[y][x])
        print(f"Беру число {matrix[y][x]}, додаю до результату, маю {arr}")
        y+=1
        step_counter += 1
    y-=1
    x-=1

    print("\nЙду ліворуч")
    while x >= offset and step_counter < cells:
        arr.append(matrix[y][x])
        print(f"Беру число {matrix[y][x]}, додаю до результату, маю {arr}")
        x-=1
        step_counter += 1
    y-=1
    x+=1
    offset+=1 #наступний напрямок руху зустріне шлях, який вже проходили. Тобто к-сть комірок, які треба не дійти до краю, збільшимо на 1

    print("\nЙду вгору")
    while y >= offset and step_counter < cells:
        arr.append(matrix[y][x])
        print(f"Беру число {matrix[y][x]}, додаю до результату, маю {arr}")
        y-=1
        step_counter += 1
    y+=1
    x+=1

print(arr)