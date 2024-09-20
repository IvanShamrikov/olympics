# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]

# ЦЮ ЗАДАЧУ ПОЯСНЮЄ ОЛЕГ, БО Я НЕ ЗМОЖУ

nums = [1,2,3]

def swap(lst, i1, i2):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp
    return lst.copy()

result = [nums]
print(f"Оголошуємо результуючий масив result і записуємо в нього початковий набір цифр {nums}")
print(f"Проходимся по індексам з початкового набору")
for i in range(len(nums)-1):
    print(f"-"*25)
    print(f"    Беремо індекс {i} з початкового набору.")
    print(f"    Проходимось по існуючим наборам перестановок {result}")
    for result_i in range(len(result)):
        print(f"        Беремо набір {result[result_i]}")
        print(f"        В ньому переставляємо цифри, починаючи з індекса {i}.")
        for nums_i in range(i + 1, len(nums)):
            print(f"            Переставляємо цифри {result[result_i][i]} і {result[result_i][nums_i]}")
            temp_lst = result[result_i].copy()
            res = swap(temp_lst, i, nums_i)
            print(f"            Отримали набір {res}, додаємо його до загального списку перестановок {result}")
            result.append(res)
print()
print(f"Ми закінчили перебирати всі варіанти наборів. Фінальний результат - {result}")

# ВАРІАНТ РІШЕННЯ РЕКУРСІЄЮ

def permute(nums):
    result = []

    def permute_rec(nums, current_index, result):
        # якщо дійшли до кінця набору цифр, записуємо перестановку в результат і завершуємо рекурсію
        if current_index == len(nums) - 1:
            result.append(nums.copy())
            return

        for index in range(current_index, len(nums)):
            # рішення схоже на моє, але рекурсія, так само беремо індекс в перестановці(current index) з якого починаємо і йдемо до кінця

            # переставили числа
            nums[current_index], nums[index] = nums[index], nums[current_index]

            # закинули новий набір в рекурсію. наприклад після першого [1,2,3] далі буде 3 виклика функції з наборами [1 2 3] [2 1 3] [3 2 1],
            # так як далі цикл буде йти з другого індексу, то отримаємо такі результати [1 2 3] -> [1 2 3] [1 3 2], [2 1 3] -> [2 1 3] [2 3 1], [3 2 1] -> [3 2 1] [3 1 2]
            # на цьому рекурсія буде завершена через перевірку на початку фунції, а кінцуві значення записані в реультуючий массив
            permute_rec(nums, current_index + 1, result)

            # переставили числа назад, так як ми переставляли їх в самому nums не використовуючи temp массив.
            nums[current_index], nums[index] = nums[index], nums[current_index]

    permute_rec(nums, 0, result)
    return result