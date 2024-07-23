# You are given a array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2


nums = [2,3,0,1,5]

near = 0 #індекс найближчого елемента
far = 0 #індекс найдальшого елемента
jumps = 0 #к-сть стрибків

while far < len(nums)-1:
    print(nums)
    farthest = 0 #з усіх індексів від near до far це буде індекс максимальногь значення.
    print(f"Розглядаємо діапазон для пошуку стрибка від індекса {near} до індекса {far}")

    for i in range(near, far+1): #ми перебираємо поточні варіанти індексів і знаходимо максимальний індекс, до якого можемо дострибнути з поточних варіантів індексів.
        print(f"Розглядаємо індекс {i}, там лежить число {nums[i]}, тобто з нього можна стрибнути на довждину {nums[i]}, тобто ми опинимось в індексі {i+nums[i]}")

        #farthest = max(farthest, i + nums[i]) #це альтернатива нижньому if

        if i+nums[i] > farthest:
            print(f"Цей стрибок на {i+nums[i]} дальший, ніж попередній максимальний стрибок {farthest}, ми оновлюємо farthest новим індексом {i+nums[i]}")
            farthest = i+nums[i]
        else:
            print(f"Цей стрибок на {i+nums[i]} виявився ближче, ніж попередній максимальний стрибок {farthest}, ми залишаємо farthest старим ({farthest})")
        input()


    near = far + 1
    far = farthest
    print(f"Тепер можна встановлювати новий діапазон пошуку максимального наступного стрибка (від {near} до {far} індекса)бо попередній діапазон ми вже перевірили.")
    jumps += 1
    input()


print(f"Наш максимальний стрибок попадає в індекс {farthest}, що вже більше за довжину масива-1, тобто ми перестрибнули кордон масиву. Кількисть стрибків = {jumps}")