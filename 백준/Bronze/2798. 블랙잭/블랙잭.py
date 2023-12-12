from itertools import combinations

N, M = map(int, input().split())
A = list(map(int, input().split()))

combi_sum = [sum(combi) for combi in combinations(A, 3) if sum(combi) <= M]

print(max(combi_sum))