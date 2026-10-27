from TEST import counter

n = 4
m = 5
fig = [[1,3], [4,2]]

min_x_fig_1_line = m+1
min_y__fig_1_line = n+1
for f in fig:
    if f[0] == 1 and f[1] < min_y__fig_1_line:
        min_y__fig_1_line = f[1]
    if f[1] == 1 and f[0] < min_x_fig_1_line:
        min_x_fig_1_line = f[0]

if min_y__fig_1_line == n+1:
    min_y__fig_1_line = 0
if min_x_fig_1_line == m+1:
    min_x_fig_1_line = 0


print(min_x_fig_1_line)
print(min_y__fig_1_line)

m = list(map(int, input().split()))
print()
