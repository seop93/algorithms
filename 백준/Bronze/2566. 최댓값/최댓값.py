answer = []
max_num = 0
n = 0
for i in range(9):
    list_n = list(map(int, input().split()))
    if max_num <= max(list_n):
        max_num = max(list_n)
        x = i + 1
        y = list_n.index(max_num) + 1

print(max_num)
print(x, y)