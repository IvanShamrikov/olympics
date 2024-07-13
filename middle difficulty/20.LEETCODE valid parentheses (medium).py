# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
import time

# Example 4:
# Input: s = "({)}"
# Output: false

# Example 5:
# Input: s = "([{}({})[]]{}{})"
# Output: true



s = "([{}({})[]]{}{})"
print(f"Строка -->> {s}")


def foo(s):

    dic = { #створюємо словник з ключами і значеннями
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = [] #пустий масив для зберігання тимчасових даних

    for l in s: #перебираємо символи в  строці
        print(f"Розглядаємо символ {l}")
        if l in dic.values(): #Якщо символ - це відкриваюча скобка, то записуємо символ в stack
            stack.append(l)
            print(f"Скобка {l} - відкриваюча, тобто складаємо в stack --> {stack}")
        elif l in dic.keys(): #Якщо символ - це закриваюча скобка, то ...
            print(f"Скобка {l} - закриваюча, робимо додаткову перевірку")
            if len(stack) == 0: # перевіряємо, якщо до цього не вносили в stack відкриваючі скобки, то значить наша закриваюча скобка не має пари.
                print(f"Масив stack пустий, тобто на цю закриваючу скобку в масиві немає ніякої відкриваючої. Це False")
                return False
            x = stack.pop()
            if  x != dic[l]: #якщо останній символ нашого stack не відповідає по типу поточній cкобці, то значить у нас збій
                print(f"Останній символ нашого stack {x} не відповідає по типу нашій закриваючій скобці {l}. Це False")
                return False
            print(f"Останній символ нашого stack {x} відповідає по типу нашій закриваючій скобці {l}. Забираємо відкриваючу скобку зі стеку, бо вона знайшла свою пару. Тепер стек виглядає так -->> {stack}")

        print("-"*20)
        time.sleep(3)

    if len(stack) != 0:
        print(f"Всі символи закінчились в строці, але в масиві відкритих скобок залишились скобки без пари --> {stack}. Це False")
        return False
    else:
        print(f"Всі символи закінчились в строці, масив stack не містить незакритих скобок, все добре, це True")
        return True

print(foo(s))

