n,m = map(int,input().split())
res = list(map(int,input().split()))

changes_x = []
changes_y = []
test = []

for i in range(n):
    test.append("k"+str(i+1))
print("test begin", test)

for _ in range(m):
    x,y = map(int,input().split())
    changes_x.append(x)
    changes_y.append(y)

for i in range(m):
    i_from = changes_x[i] -1
    i_to = changes_y[i] -1
    test[i_to] = test[i_from]
print("test fin", test)

print(f"res = {res}")
# Словник для збереження значень кожного початкового джерела
source_values = {}

# Перевірка кінцевих карток на узгодженість
for i in range(n):
    s = test[i]    # початкове джерело, з якого сформувалась поточна картка
    val = res[i]   # кінцеве значення на картці
    print(f"s = {s}, val = {val}")

    if s not in source_values:
        source_values[s] = val
        print(source_values)
        ans = len(source_values)
    else:
        if source_values[s]!=val:
            ans = -1
            break
print(ans)

