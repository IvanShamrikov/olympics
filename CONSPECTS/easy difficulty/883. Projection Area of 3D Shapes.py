 # Picture: https://leetcode.com/problems/projection-area-of-3d-shapes/description/
 #
 # You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
 # Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
 # We view the projection of these cubes onto the xy, yz, and zx planes.
 # A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane.
 # We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
 # Return the total area of all three projections.
 #
 # Input: grid = [[1,2],[3,4]]
 # Output: 17
 # Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
 #
 # Example 2:
 # Input: grid = [[2]]
 # Output: 5
 #
 # Example 3:
 # Input: grid = [[1,0],[0,2]]
 # Output: 8


grid = [[1,2],[3,4]]
print(f"Схема висоток в місті = {grid}")
xy = 0 #тіні на землі
xz = 0 #бокові тіні по стороні Х
yz = 0 #бокові тіні по стороні У
maximum = 0 #технічна змінна для знаходження найбільшого будинку на вулиці, який відкидуює тінь, що поглинає всі інші тіні.

for i in range(len(grid)):
    print(f"Розглядаємо вулицю {i} по горизонталі X. Там стоять такі будинки =  {grid[i]}")
    xz += max(grid[i])
    print(f"На сторону XZ буде падати тінь найвищого будинку  = {max(grid[i])}, додаємо її значення до загального лічільника тіней по стороні XZ. Це буде {xz} клітин")

    maximum = 0 #скидаємо показник макусимальної тіні по yz

    print(f"Проходимось по вертикальним будинками.")
    for j in range (len(grid[i])):
        print(f"Ідемо по стовпчику {i} і рядку {j}")
        if grid[i][j] > 0:
            xy += 1
            print(f"Тут стоїть дім висотою {grid[i][j]}. По підлозі xy він займає 1 клітину. Додаємо +1 до загального лічільника тіней по землі XУ ")
        else:
            print(f"Тут стоїть дім висотою {grid[i][j]}. Тобто дім не стоїть, тіні неа землю не відбрасує, нічого не додаємо до загального лічільника тіней по землі XУ ")

        print(f"Ідемо стовпчику {j} і рядку {i}")
        if grid[j][i] > maximum:
            print(f"Тут стоїть дім висотою {grid[j][i]}. Його висота поки є найбільшою серед вертикалі, тому запамятаємо його тінь як найвищу поки шо")
            maximum = grid[j][i]
        else:
            print(f"Тут стоїть дім висотою {grid[j][i]}. Його висота не перевищує висоту попереднього найбільшого будинку в цій вертикалі ({maximum}), тому тінь по цій вертикалі залишається {maximum}")


    yz += maximum

print(f"xy = ", xy)
print(f"xz = ", xz)
print(f"zy = ", yz)
print(xy + xz + yz)
