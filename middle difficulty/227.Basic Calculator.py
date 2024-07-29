 # Given a string s which represents an expression, evaluate this expression and return its value.
 # The integer division should truncate toward zero.
 # You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
 # Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
 #
 # Example 1:
 # Input: s = "3+2*2"
 # Output: 7
 #
 # Example 2:
 # Input: s = " 3/2 "
 # Output: 1
 #
 # Example 3:
 # Input: s = " 3+5 / 2 "
 # Output: 5
import math
def calculate(string: str) -> int:
        num = 0
        PreSign = '+' #попередній знак, по дефолту +
        stack = [] #куди ми закидуємо числа, які ми зчитуємо за строки

        for c in string+'+': #проходимось по строці посимвольно, додавання '+' потрібно щоб додати в стеку останнє число (зайти в elif і додати в масив)
            if c.isdigit(): #якщо це цифра, то додаємо його до числа num, попередньо піднявши розряд числа num.
                num = num * 10 + int(c)
            elif c in "+-*/": #якщо символ - це не цифра
                if PreSign=='+':  # якщо попередній знак був +
                    stack.append(num)  #додаємо число до масива, щоб в кінці при складанні всіх елементів масиву воно додалось
                elif PreSign == '-': # якщо попередній знак був -
                    stack.append(-num) #додаємо число до масива, але негативне, щоб в кінці при складанні всіх елементів масиву іоно віднялось
                elif PreSign == '*': # якщо попередній знак був *
                   stack.append(stack.pop()*num) #з масиву беремо останній елемент, множимо його на поточне число і записуємо добуток назад
                elif PreSign == '/': # якщо попередній знак був /
                    stack.append(math.trunc(stack.pop()/num)) #з масиву беремо останній елемент, ділимо його на поточне число, округлюємо і записуємо результат назад
                PreSign=c #оновлюємо попередній знак
                num=0 #оновлюємо число num
        return sum(stack) #робимо суму всіх елементів масиву і повертаємо назовні

print(calculate(" 33 + 14 / 2 "))