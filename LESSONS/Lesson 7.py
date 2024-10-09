#------------------------------------------------------


# Посміхайлики
#
# Під час олімпіади з програмування журі та оргкомітет полюбляють спостерігати за перебігом подій.
# Щоб було веселіше та цікавіше голова журі малює крейдою на дошці посміхайлики:
# - коли будь-хто з учасників олімпіади здає задачу на максимальний бал, голова журі малює на дошці такий посміхайлик: :-).
# - коли виявляється, що на дошці намальовано три посміхайлика :-), голова журі стирає ці посміхайлики, а замість них малює такий посміхайлик ;-).
# - коли виявляється, що на дошці намальовано п'ять посміхайликів ;-), голова журі стирає ці посміхайлики, а замість них малює такий посміхайлик «:-D».
# - коли виявляється, що на дошці намальовано сім посміхайликів :-D, голова журі стирає ці посміхайлики, а замість них малює такий посміхайлик «;-D».
# Ось так буде змінювати набір посміхайликів на дошці голова журі:
#
# Перше правильне рішення        :-)
# Друге правильне рішення        :-):-)
# Трете правильне рішення        :-):-):-)               голова журі стирає ці три посміхайлики,
#                                ;-)                    а замість них малює один ;-)
# Четверте правильне рішення     ;-):-)
# П'яте правильне рішення        ;-):-):-)
# Шосте правильне рішення        ;-):-):-):-)           голова журі стирає останні три посміхайлики,
#                                ;-);-)                 а замість них малює один ;-)
# Сьоме правильне рішення        ;-);-):-)
# Восьме правильне рішення       ;-);-):-):-)
# Дев'яте правильне рішення      ;-);-):-):-):-)            голова журі стирає останні три посміхайлики,
#                                ;-);-);-)              а замість них малює один ;-)
# Десяте правильне рішення       ;-);-);-):-)
# Одинадцяте правильне рішення   ;-);-);-):-):-)
# Дванадцяте правильне рішення   ;-);-);-):-):-):-)     голова журі стирає останні три посміхайлики,
#                                ;-);-);-);-)           а замість них малює один ;-)
# Тринадцяте правильне рішення   ;-);-);-);-):-)
# Чотирнадцяте правильне рішення ;-);-);-);-):-):-)
# П'ятнадцяте правильне рішення  ;-);-);-);-):-):-):-)  голова журі стирає останні три посміхайлики,
#                                ;-);-);-);-);-)        а замість них малює один ;-)
#                                :-D                    а потім п'ять посміхайликів ;-) заміняє на :-D
# ...  ...  ...   ...   ...   ...   ...   ...  ...   ...   ...  ...
# Сто сорокове правильне рішення ;-D:-D:-D;-):-):-)
#
# Напишіть програму, яка з'ясує, що буде намальовано на дошці голови журі після того, як буде здано N-те правильне рішення.
#
# У вхідних даних записано натуральне число N (1≤N≤32767).
#
# Виведіть, що буде намальовано на дошці голови журі після того, як буде здано N-те правильне рішення


N = int(input("N = "))
first = 0
second = 0
third = 0
fourth = 0

first = N
first_remaining = N%3
second = first//3
second_remaining = second%5
third = second//5
third_remaining = third%7
forth = third//7

firstSmile = ":-)"
secondSmile = ";-)"
thirdSmile = ":-D"
fourthSmile = ";-D"


print(fourthSmile * forth, thirdSmile * third_remaining, secondSmile * second_remaining, firstSmile * first_remaining)



#------------------------------------------------------


# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:
#
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
#
#
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# var removeDuplicates = function (ar) {
#     // const arr = [];
#     // for(let i = 0; i < nums.length; i++){
#     //     if(!arr.includes(nums[i])){
#     //         arr.push(nums[i]);
#     //     }else{
#     //         nums.splice(i, 1);
#     //         i--;
#     //     }
#     // }
#     // return nums.length
#
#     let n = ar.length;
#     let i = 0, k = 0;
#
#     for (let i = 0; i < n; i++) {
#         if (ar[i] > ar[k])
#             ar[++k] = ar[i];
#     }
#
#     return k + 1;
# };



nums = [0,0,1,1,1,2,2,3,3,4]

# РІШЕННЯ 1
# print(set(nums))

#РІШЕННЯ 2
l = len(nums)
k = 0 #індекс поточного унікального числа

print("Наш масив ---> ", nums)
for i in range(l):
    print(f"Поточний унікальний індекс k({k}), там лежить число {nums[k]}")
    print(f"Розглядаємо число за індексом i({i}) --> {nums[i]}")
    if nums[i] > nums[k]: #якщо наступне число більше за попереднє унікальне
        print(f"{nums[i]} більше за {nums[k]}, тобто треба додати/перезаписати че число {nums[i]} на наступне місце k({k+1}) за поточним унікальним k({k})")
        k+=1 #ми збільшуємо індекс унікального числа
        nums[k] = nums[i] #перезаписуємо наше число на місце для цнікального числа
        print("Перезаписали ячейку, тепер масив виглядає --> ", nums)
        print("-" * 20)
        continue
    print(f"Число {nums[i]} по індексу i({i}) меньше або дорівнює останньому унікальному {nums[k]} по індексу k({k}). Шукаємо далі")
    print("-"*20)

print("Увесь відсортований масив --> ", nums)
print("Обрізаний масив тільки з унікальними числами --> ", nums[:k+1])


#------------------------------------------------------

# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Example 2:
# Input: n = 2
# Output: false

#ПЕРЕД СТАРТОМ ЗАДАЧІ ТРЕБА ПРОГОВОРИТИ, ЩО ЧИСЛО БУДЕ ЩАСЛИВИМ, ЯКЩО НА ЯКОМУСЬ ЕПАТІ ВОНО ПЕРЕТВОРИТЬСЯ НА 1 АБО 7.
#БО ТІЛЬКИ ЦІ ЦИФРИ В КІНЦІ КІНЦІВ МОЖУТЬ СТАТИ ЩАСЛИВИМИ

n = 7
print("Початкове число =", n)

while True:
    print("-"*25)
    n = str(n)
    lst = list(n)
    n = 0
    print(f"Маємо такі числа -> {lst}")
    for i in range(len(lst)):
        lst[i] = int(lst[i])
        n = n + lst[i]**2
    print(f"Сума квадратів чисел = {n}")

    if n < 10:
        print(f"Сума квадратів чисел меньше 10.")
        if n == 7:
            continue
        if n == 1:
            print(f"Це число 1. Тобто початкове число було щасливим.")
            print(True)
        else:
            print(f"Це число не дорівнює 1. Тобто початкове число не було щасливим.")
            print(False)
        break