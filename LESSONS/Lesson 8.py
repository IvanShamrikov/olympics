#Fibonacci

#Заняття потребує лекції про рекурсію

 # The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
 # F(0) = 0, F(1) = 1
 # F(n) = F(n - 1) + F(n - 2), for n > 1.
 # Given n, calculate F(n).
 #
 # Example 1:
 # Input: n = 2
 # Output: 1
 # Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
 #
 # Example 2:
 # Input: n = 3
 # Output: 2
 # Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
 #
 # Example 3:
 # Input: n = 4
 # Output: 3
 # Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

def fib(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))

#-------------------------------------------
#Знаходження n-го числа фібоначі РЕКУРСИВНОЮ функцією

counter = 0 #лічильник, який виводить кількість викликів функції
def fib_rec(number):
    global counter
    counter += 1
    if number == 1 or number == 2:
        return 1
    else:
        return fib_rec(number-1) + fib_rec(number-2)
print(fib_rec(10))
# print(fib_rec(20))
# print(fib_rec(40))
print(counter)

#-------------------------------------------
#Знаходження n-го числа фібоначі РЕКУРСИВНОЮ функцією
def fib(num, n1, n2):
    print(n1 + n2)
    if (num - 1 >= 0):
        return fib(num - 1, n1 + n2, n1)

fib(10, 1, 1)

#-------------------------------------------
#Знаходження n-го числа фібоначі Лінійною функцією

def fib_lin(number, counter):
    fib1, fib2 = 1, 2
    number = number -2
    while number > 0:
        fib_next = fib1 + fib2
        fib1, fib2 = fib2, fib_next
        number -= 1
        counter += 1
    return fib2

counter = 0
print(fib_lin(10, counter))
print(counter)

#-------------------------------------------
#Знаходження n-го числа фібоначі Лінійною функцією за допомогою масива list
counter = 0
def fib_list(number):
    lst = [1,1]
    number -= 2
    while number > 0:
        number -= 1
        lst.append(lst[-1]+lst[-2])
        global counter
        counter +=1
    return(lst[-1])

print(fib_list(10))
print(counter)