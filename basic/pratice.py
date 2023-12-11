def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            answer.extend([arr[i]] * 2)

    return answer


print(solution([3, 4, 2], [True, False, True]))