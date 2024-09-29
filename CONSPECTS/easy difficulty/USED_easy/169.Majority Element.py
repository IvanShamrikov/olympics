 # Given an array nums of size n, return the majority element.
 # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 #
 # Example 1:
 # Input: nums = [3,2,3]
 # Output: 3
 #
 # Example 2:
 # Input: nums = [2,2,1,1,1,2,2]
 # Output: 2

# Наданий масив чисел, треба знайти значення, що є модавлячою більшістю (за умовою таке число існує, тобто його кількість більша за n/2)

#------------------------------------
#РІШЕННЯ ЗА ДОПОМОГОЮ СОРТУВАННЯ
#Можна відсортувати масив, і взяти число посередині. так як наше шукане має к-сть більше за половину масива, серединка в будь-якому випадку буде репрезентцвати шукане

#Сортування + взяти середину

#------------------------------------
#РІШЕННЯ ЗА ДОПОМОТОЮ ПЕРЕБОРУ

def finder(nums):
    dic = {} #словник для ключа (число), значення (к-сть входжень)
    max = 0 #максимальне входження
    majorityNumber = 0 #число, яке максимально входить

    print(f"Переберемо всі елементи масиву {nums}")
    for el in nums:
        print("-"*20)
        print(f"Беремо число {el}")
        if el not in dic:
            print("Такого числа ще немає в словнику, додаємо його туди як ключ і даємо йому значення 1 (к-сть входжень).")
            dic[el] = 1
            print(dic)
        else:
            print("Таке число вже є словнику, додаємо йому до ключа значення 1 (к-сть входжень +1).")
            dic[el] += 1
            print(dic)

        if dic[el] > max:
            print(f"Оу, кількість входжени числа {el} = {dic[el]} і воно перевищило попередній максимум ({max})! Тож тепер чило {el} з к-стью входжень {dic[el]} є новим максимумом")
            max = dic[el]
            majorityNumber = el


    print(f"Ми пройшли увесь масив, максимальне входження число {majorityNumber} ({dic[majorityNumber]} разів)")
    return majorityNumber

nums = [2,2,1,1,1,2,2]
result = finder(nums)
print(result)


# рішення номер 2
nums = [2,2,1,1,1,2,2]
for el in nums:
    if nums.count(el) > len(nums)/2:
        print(el)
        break

