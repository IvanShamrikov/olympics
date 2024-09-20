 # Given a sorted array of distinct integers and a target value, return the index if the target is found.
 # If not, return the index where it would be if it were inserted in order.
 # You must write an algorithm with O(log n) runtime complexity.
 #
 #
 # Example 1:
 # Input: nums = [1,3,5,6], target = 5
 # Output: 2
 #
 # Example 2:
 # Input: nums = [1,3,5,6], target = 2
 # Output: 1
 #
 # Example 3:
 # Input: nums = [1,3,5,6], target = 7
 # Output: 4

nums = [1,3,5,6]
target = 4

def finder(nums, target):
    left = 0
    right = len(nums) - 1
    print(f"Починаю пошук з лівого ({left}) та правого ({right}) індексів масива {nums} в пошуку індекса нашого числа {target}")
    while left < right:
        center = round((left + right) / 2)
        print(f"Шукаю індекс посередині між {left} та {right} = {center} в масиві {nums} ")
        if nums[center] == target:
            print(f"За індексом {center} ми знайшли шукане число {target}. Індекс {center} є відповіддю задачі")
            return
        elif nums[center] < target:
            print(f"Число за індексом {center} ({nums[center]}) меньше за наше шукане {target}. Беремо праву частину масива і шукаємо далі.")
            left = center + 1
        elif nums[center] > target:
            print(f"Число за індексом {center} ({nums[center]}) більше за наше шукане {target}. Беремо ліву частину масива і шукаємо далі.")
            right = center - 1
        input()
        print("-"*20)

    print(f"Закінчили пошук, не знайшли шукане число {target} в масиві {nums}. Тому шукаємо індекс, де шукане число повинно було б стояти")
    center = round((left + right) / 2)
    if nums[center] > target:
        print(f"Останній серединний індекс, на якому ми зупинились, був {center}. По ньому в масиві стоїть число {nums[center]}. Воно більше ніж шукане число {target}, тому шукане число як раз треба вставити в цей індекс {center}. Цей індекс і буде відповіддю задачі")
    else:
        print(f"Останній серединний індекс, на якому ми зупинились, був {center}. По ньому в масиві стоїть число {nums[center]}. Воно меньше ніж шукане число {target}, тому шукане число як раз треба вставити в наступний індекс {center+1}. Цей індекс і буде відповіддю задачі")


finder(nums, target)