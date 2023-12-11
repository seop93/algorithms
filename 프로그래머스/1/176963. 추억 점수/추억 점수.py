def solution(name, yearning, photo):
    dict_sol = {key: value for key, value in zip(name,yearning)}
    answer = []
    for i in range(len(photo)):
        total_score = 0
        for j in photo[i]:
            if j in dict_sol:
                total_score += dict_sol[j]
        answer.append(total_score)

    return answer
