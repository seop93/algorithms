total = 0
total_g = 0
dict_score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for n in range(20):
    s, v, g = input().split()
    if g == 'P':
        continue
    total += float(v) * dict_score[g]
    total_g += float(v)

print(total/total_g)