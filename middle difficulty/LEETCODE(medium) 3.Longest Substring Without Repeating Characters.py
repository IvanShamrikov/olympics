# // Given a string s, find the length of the longest substring without repeating characters
#
# // Example 1:
# // Input: s = "abcabcbb"
# // Output: 3
# // Explanation: The answer is "abc", with the length of 3.
#
# // Example 2:
# // Input: s = "bbbbb"
# // Output: 1
# // Explanation: The answer is "b", with the length of 1.
#
# // Example 3:
# // Input: s = "pwwkew"
# // Output: 3
# // Explanation: The answer is "wke", with the length of 3.
#
# // Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.





s = "aBcaBqwertyuBcBB"
letters = "" #неповнторювальні букви
res = 0 #довжина найбільшої наповторювальної строки

for i in range(len(s)): #перебираємо індекси букв нашого слова
    if s[i] not in letters:  #Якшо букви не було в letters - значить, вона ще не повторювалась
        letters += s[i] #додаємо літеру до підстроки

    else:   #сюди падають варіанти, коли зустрічається перша повторювальна літера.
        if len(letters) > res : #якщо довжина унікальної підстроки більша за попереднью максимальну довжину
            res = len(letters) #оновлюємо число максимума
        else:
            letters = s[i] #скидуємо підстроку до літери, яка почала повторюватись, підстрока тепер починається з цієї літери.

print(res)