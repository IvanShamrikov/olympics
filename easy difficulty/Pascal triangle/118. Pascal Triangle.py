 # Given an integer numRows, return the first numRows of Pascal's triangle.
 # In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
 #
 # Example 1:
 # Input: numRows = 5
 # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 #
 # Example 2:
 # Input: numRows = 1
 # Output: [[1]]


def print_pyramid(list):
    lenght = len(list)
    for row_num in range(len(list)):
        spaces = lenght - row_num
        print(" " * spaces, end="")
        print(list[row_num])

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
    print_pyramid(list)


