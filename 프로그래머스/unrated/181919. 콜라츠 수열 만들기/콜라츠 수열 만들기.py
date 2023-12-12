def solution(n):
    result = [n]  # 초기값 n을 수열에 추가
    
    while n != 1:  # n이 1이 될 때까지 반복
        if n % 2 == 0:  # 짝수일 경우
            n //= 2
        else:  # 홀수일 경우
            n = 3 * n + 1
        result.append(n)  # 계산된 값 n을 수열에 추가
        
    return result  # 콜라츠 수열 반환