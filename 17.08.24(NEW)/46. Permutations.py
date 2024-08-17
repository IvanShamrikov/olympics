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