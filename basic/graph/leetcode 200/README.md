# leetcode - 739

[문제 링크](https://leetcode.com/problems/number-of-islands/)

### 분류

Graph Brute Force

### 문제 설명

주어진 2D 그리드 맵에서 '1'로 표시된 섬의 개수를 세는 문제입니다. 이 문제에서 섬은 수직 또는 수평으로 인접한 '1'로 이루어진 땅의 영역을 나타냅니다.
대각선으로 인접한 땅은 인접한 것으로 간주하지 않습니다.

제한 조건:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j]는 '0' 또는 '1'입니다.

### 입력

```python
grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]  # example1

```

### 출력

```python
1 # example1
```
