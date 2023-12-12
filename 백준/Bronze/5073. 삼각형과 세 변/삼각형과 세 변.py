answer = []
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
        answer.append("Invalid")
        continue

    count = set([a, b, c])

    if len(count) == 1:
        answer.append("Equilateral")
    elif len(count) == 2:
        answer.append("Isosceles")
    else:
        answer.append("Scalene")

print('\n'.join(answer))
