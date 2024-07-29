 # https://leetcode.com/problems/island-perimeter/description/
 # You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
 # Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
 # is exactly one island (i.e., one or more connected land cells).
 # The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square
 # with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
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