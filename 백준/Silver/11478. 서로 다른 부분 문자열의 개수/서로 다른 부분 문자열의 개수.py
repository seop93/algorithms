import sys

S = sys.stdin.readline().rstrip()

count = set()

for i in range(0, len(S)):
    for j in range(i, len(S)):
        count.add(S[i:j+1])

print(len(count))