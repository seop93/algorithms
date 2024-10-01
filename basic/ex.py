# O(N)
for i in range(n):
    print("proc")

## 리스트에서 최대값을 찾는 경우
def find_max(arr):
    max_value = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

# O(1)
a = 7
b = 34
print("hello")
a = [1,2,3,4,5,6] # O(N)

## 상수 번 반복 = O(1) / input에 따라서 반복 횟수가 정해지는게 아닌 경우
int(n)
for i in range(100):
    print(n)

# O(n^2)

## O(2n^2)
n = 10 # N을 원하는 값으로 설정
for i in range(n):
    print("hello")

for j in range(n):
    print("bye")

## O(n^2)
n = 10 # N을 원하는 값으로 설정
for i in range(N):
    for j in range(N):
        print("hello")

# O(nm)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 4, 5, 6, 7, 8]
common = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            common.append(list1[i])

# 함수, 연산자, 메서드의 시간복잡도

## 총 7개의 방이 존재한다고 가정
## visited는 지금까지 방문한 모든 방의 번호를 저장
## list를 반복 하는 in 으로 접근
visited = [0, 1, 3, 5]
if 3 in visited: # O(N)
    print("room number 3 visited")

for node in visited:
    print(node)

visited = [True , True, False, True, False, True, False]
# if visited[3] == True;
if visited[3]:
    print("room number 3 visited") #인덱스스로 접근하기 때문에 O(1)

## hashtable
visited = {0:True, 1:True, 2:True, 3:True}
if 3 in visited: #O(1)
    print("room number 3 visited")

visited = set()
visited = {0, 1, 3, 5}
if 5 in visited: # O(1)
    print("room number 5 visited")

# sort() - O(nlogn)
# heappush() / heappush() - O(logn)
# deque
import time
from collections import deque

# Deque를 사용한 예제
def deque_example():
    dq = deque()
    start_time = time.time()

    # 맨 앞에 100000번 요소 추가
    for i in range(100000):
        dq.append(i)

    # 맨 앞에 100000번 요소 제거
    for i in range(100000):
        dq.popleft()

    end_time = time.time()
    print(f"Deque작업시간: {end_time - start_time} 초")

# List 사용한 예제
def list_example():
    lst = []
    start_time = time.time()

    # 맨 앞에 100000 번 요소 추가
    for i in range(100000):
        lst.append(i)

    # 맨 앞에 100000 번 요소 제거
    for i in range(100000):
        del lst[0]

    end_time = time.time()
    print(f"List 작업 시간: {end_time - start_time} 초")


# 시간복잡도 심화

## for - while 중첩 되었다고 O(n^2)이 아니다

def longestConsecutive(arr):
    nums = set(nums) # O(N) 중복된 숫자를 없애기 위함
    answer = 0

    for num in nums: # O(N)
        if num - 1 not in nums:
            cnt = 1
            while num + 1 in nums:
                num += 1
                cnt += 1
            answer = max[answer, cnt]

    return answer






