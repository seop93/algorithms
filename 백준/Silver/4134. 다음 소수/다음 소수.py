import sys, math
def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
for _ in range(n):
    n = int(sys.stdin.readline())
    while True:
        if prime(n):
            print(n)
            break
        else:
            n += 1