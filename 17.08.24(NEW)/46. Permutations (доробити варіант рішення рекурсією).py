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

