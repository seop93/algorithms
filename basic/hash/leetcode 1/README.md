# leetcode - 739

[문제 링크](https://leetcode.com/problems/two-sum/)

### 분류

hash table을 이용한 자료구조

### 문제 설명

주어진 정수 배열 nums와 정수 target이 주어졌을 때, 두 숫자의 합이 target이 되는 인덱스를 반환하는 문제입니다.

각 입력에 정확히 하나의 해결책이 있고, 동일한 요소를 두 번 사용할 수 없다고 가정합니다. 반환 순서는 어떤 순서든 상관 없습니다.

제한 조건:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

### 입력

```python
nums = [2,7,11,15], target = 9  # example1
nums = [3,2,4], target = 6  # example2

```

### 출력

```python
[0,1]  # example1
[1,2]  # example2
```
