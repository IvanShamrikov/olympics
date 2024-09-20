# // Given a string s consisting of words and spaces, return the length of the last word in the string.
# // A word is a maximal substring consisting of non-space characters only.
#
# // Example 1:
# // Input: s = "Hello World"
# // Output: 5
# // Explanation: The last word is "World" with length 5.
# //
# // Example 2:
# // Input: s = "   fly me   to   the moon  "
# // Output: 4
# // Explanation: The last word is "moon" with length 4.
# //
# // Example 3:
# // Input: s = "luffy is still joyboy"
# // Output: 6
# // Explanation: The last word is "joyboy" with length 6.

string = "luffy is still joyboy      "

#РІШЕННЯ 1
lst = string.split()
last_word = lst[len(lst)-1]
print(len(last_word))

#РІШЕННЯ 2
string = "luffy is still joyboy      "

counter = 0
for i in range(len(string)-1, -1, -1):
    if string[i] == " " and counter > 0:
        break
    elif string[i] != " ":
        counter += 1
print(counter)

