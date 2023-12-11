def solution(string):
    answer = [0] * 52
    for s in string:
        if s.isupper():
            answer[ord(s) - 65] += 1
        else:
            answer[ord(s) - 71] += 1
    
    return answer