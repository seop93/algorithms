# leetcode - 739

[문제 링크](https://leetcode.com/problems/daily-temperatures/)

### 분류

stack 자료구조

### 문제 설명

문제: 일일 온도 목록이 주어졌을 때, 각 날짜마다 다음으로 따뜻해지는 날짜까지의 기간을 계산하려고 합니다. 더 따뜻한 날짜가 없는 경우, 0으로 표시합니다.

함수의 입력은 정수 배열 temperatures로 주어지며, 출력은 정수 배열로 반환해야 합니다. 각 날짜마다 다음으로 따뜻해지는 날짜까지의 기간을 나타내는 배열을 반환해야 합니다.

제한 조건:

- 1 <= temperatures.length <= 105
- 30 <= temperatures[i] <= 100

### 입력

```python
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]  # example1
temperatures = [30,40,50,60]  # example2

```

### 출력

```python
[1, 1, 4, 2, 1, 1, 0, 0]  # example1
[1,1,1,0]  # example2
```