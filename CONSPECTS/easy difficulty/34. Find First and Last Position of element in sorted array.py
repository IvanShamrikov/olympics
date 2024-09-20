 # Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
 # If target is not found in the array, return [-1, -1].
 # You must write an algorithm with O(log n) runtime complexity.
 #
 # Example 1:
 # Input: nums = [5,7,7,8,8,10], target = 8
 # Output: [3,4]
 #
 # Example 2:
 # Input: nums = [5,7,7,8,8,10], target = 6
 # Output: [-1,-1]
 #
 # Example 3:
 # Input: nums = [], target = 0
 # Output: [-1,-1]

nums = [5,7,7,8,8,10]
target = 8
print(f"Маємо масив {nums}, шукаємо індекси початку і кінця входження числа {target}")
def finder(nums, target):
    left = 0
    right = len(nums) - 1

    start = None
    end = None


    if len(nums) == 0:
        print("Початковий масив пустий, відповідь задачі:", end = " ")
        return [-1,-1]
    if len(nums) == 1:
        if nums[0] == target:
            print(f"Початковий масив містить 1 число і це наше число {target}, відповідь задачі:", end=" ")
            return [0,0]
        else:
            print(f"Початковий масив містить 1 число і це не наше число {target}, відповідь задачі:", end=" ")
            return [-1, -1]

    while left <= right:
        center = round((left + right) / 2)
        print(f"Шукаю індекс посередині між {left} та {right} = {center} в масиві {nums}. Там стоїть число {nums[center]}")
        if nums[center] == target:
            print(f"За індексом {center} ми знайшли шукане число {target}. тепер треба знайти індекси початку і кінця входження цього числа в масиві")
            start = center
            end = center

            while nums[start] == target:
                print(f"Ідемо ліворуч від індекса {start}. там стоїть число {nums[start]}.")
                start -= 1
                if start < 0 or nums[start] != target:
                    print(f"Ми закінчили пошук, самий лівий індекс числа {target} був індексом {start+1}")
                    start += 1
                    break

            while nums[end] == target:
                print(f"Ідемо праворуч від індекса {end}. там стоїть число {nums[end]}.")
                end += 1
                if end >= len(nums) or nums[end] != target:
                    print(f"Ми закінчили пошук, самий правий індекс числа {target} був індексом {end + 1}")
                    end -= 1
                    break

            break

        elif nums[center] > target:
            print(f"Число за індексом {center} ({nums[center]}) більше за наше шукане {target}. Беремо ліву частину масива і шукаємо далі.")
            right = center - 1
        elif nums[center] < target:
            print(f"Число за індексом {center} ({nums[center]}) меньше за наше шукане {target}. Беремо праву частину масива і шукаємо далі.")
            left = center + 1

    if start != None and end != None:
        print("Ми знайшли число та його індекси входження. Відповідь: ", end = "")
        return [start, end]
    else:
        print("Ми не знайшли число в масиві. Відповідь: ", end = "")
        return [-1, -1]

print(finder(nums, target))