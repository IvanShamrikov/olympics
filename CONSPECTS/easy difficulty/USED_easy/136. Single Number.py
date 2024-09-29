 # Дано непорожній масив цілих чисел nums, де кожен елемент з'являється двічі, за винятком одного. Знайдіть це єдине число.
 # Ви повинні реалізувати розв'язок з лінійною складністю часу та використовувати тільки константний додатковий простір.
 #
 # Example 1:
 # Input: nums = [2,2,1]
 # Output: 1
 #
 # Example 2:
 # Input: nums = [4,1,2,1,2]
 # Output: 4
 #
 # Example 3:
 # Input: nums = [1]
 # Output: 1

nums = [4,1,2,1,2]
dic = {}

for x in nums:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for key in dic:
    if dic[key] == 1:
        print(key)