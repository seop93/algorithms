# leetcode - 739

[문제 링크](https://leetcode.com/problems/keys-and-rooms/)

### 분류

Graph DFS

### 문제 설명

주어진 정수 배열 nums와 정수 target이 주어졌을 때, 두 숫자의 합이 target이 되는 인덱스를 반환하는 문제입니다.

각 입력에 정확히 하나의 해결책이 있고, 동일한 요소를 두 번 사용할 수 없다고 가정합니다. 반환 순서는 어떤 순서든 상관 없습니다.

제한 조건:

- n == rooms.length
- 2 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique.

### 입력

```python
rooms = [[1],[2],[3],[]]  # example1
rooms = [[1,3],[3,0,1],[2],[0]]  # example2

```

### 출력

```python
Output: true # example1
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.  

Output: false   # example2
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

```
