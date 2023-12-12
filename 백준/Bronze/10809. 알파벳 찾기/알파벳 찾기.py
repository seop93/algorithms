data = input()
alpha = [-1]*26
for i in range(len(data)):
    if alpha[ord(data[i])-97] == -1:
        alpha[ord(data[i])-97] = i

print(' '.join(str(i) for i in alpha))