# Арифметика

# Молодший брат Степана Мишко навчається у першому класі.
# Він дуже допитливий і постійно дістає Степана запитаннями: А скільки? А чому?
# Сьогоднішній день не виключення.
# Мишко  каліграфічно виписує цифри в ряд і запитує: А скільки різних цифр у записі цього числа.
# На перші приклади Степан швидко знаходив відповідь.
# Але Мишко чим далі, тим більші числа записував.
# Це стало для Степана проблемою.

# Допоможіть Степану, напишіть програму, яка визначає, кількість різних цифр у числі Мишка.
# Формат вхідних даних: перший рядок вхідного файлу містить одне ціле число N(1 ≤ N ≤ 10^1000), записане Мишком.
# Формат вихідних даних: вихідний файл має містити одне число – кількість різних цифр у числі.
#
# Приклад вхідних і вихідних даних:
# count.in - 1233
# count.out - 3

# ---------------------------
# перший варіант

x = input()
y = set(x) #використовуємо масив типу set(кучу), який зберігає тільки унікальні значення
print(len(y))

# ---------------------------
# другий варіант

x = list(input())

res = []
for i in x:
    if i not in res:
        res.append(i)

print(len(res))

