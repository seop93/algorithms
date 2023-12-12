M = int(input())
N = int(input())
answer = []
for num in range(M, N+1):
    e = 0
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                e += 1
                break
        if e == 0:
            answer.append(num)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))

