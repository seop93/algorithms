n, m = map(int, input().split())

mr = []
cnt = []
for i in range(n):
    mr.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        w_index = 0
        b_index = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if mr[i][j] != 'W':
                        w_index += 1
                    else:  # W일 때
                        b_index += 1
                else:  # 홀수인 경우
                    if mr[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1

        cnt.append(w_index)
        cnt.append(b_index)
print(min(cnt))