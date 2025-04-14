# Вам дано рядок jewels, що представляють типи каменів, які є коштовностями, і рядок stones, що представляє камені, які ви маєте.
# Кожен символ у рядку stones є типом каменю, який ви маєте. Ви хочете дізнатися, скільки з ваших каменів також є коштовностями.
# Літери чутливі до регістру, тому "a" вважається іншим типом каменю, ніж "A".

 # Example 1:
 # Input: jewels = "aA", stones = "aAAbbbb"
 # Output: 3

 # Example 2:
 # Input: jewels = "z", stones = "ZZ"
 # Output: 0


jewels = "aA"
numJewelsInStones = 0
stones = "aAAbbbb"

counter = 0
for i in stones:
    if i in jewels:
        counter += 1

print(counter)

