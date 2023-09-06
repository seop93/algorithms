# leetcode - 739

[문제 링크](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/)

### 분류

Graph BFS

### 문제 설명

주어진 n x n 이진 행렬 그리드에서 가장 짧은 클리어 경로의 길이를 반환합니다. 클리어 경로가 없으면 -1을 반환합니다.

이진 행렬에서의 클리어 경로란 다음과 같은 조건을 만족하는 경로를 의미합니다

1. 경로의 모든 방문한 셀은 0이어야 합니다.
2. 경로의 인접한 셀들은 8방향으로 연결되어 있어야 합니다. 즉, 서로 다르며 가장자리나 모서리를 공유해야 합니다.
3. 클리어 경로의 길이는 이 경로의 방문한 셀의 수입니다.

제한 조건:

- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

### 입력

```python
grid = [[0,0,0],[1,1,0],[1,1,0]]  # example1
grid = [[1,0,0],[1,1,0],[1,1,0]]  # example2

```

### 출력

```python
4  # example1
-1  # example2
```
