def solution(arr):
    result = []
    for a in arr:
        result.extend([a] * a)
    return result