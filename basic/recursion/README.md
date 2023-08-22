# recursion

## 구성요소 2가지

`recurremce ralation` => 점화식

- problem와 subproblem의 관계식을 말합니다.

`base case`

- 더이상 재귀호출을 하지 않아도 계산값을 반환할 수 있는 상황(조건)을 말합니다.
- 모든 입력이 최종적으로 base case를 이용해서 문제를 해결할 수 있어야 합니다.
- basecase가 무조건 있ㅇ어야 재귀함수의 무한루프를 방지할 수 있습니다.

## 시간복잡도

시간복잡도
재귀함수 전체 시간복잡도는 재귀 함ㅅ 호출 수X(재귀 함수 하나당) 시간복잡도
> Excution Tree(recursion tree): 재귀 함수의 실행 흐름을 나타내는 데 사용되는 트리

O(n)n에 비례한 호출
recurrence relation: f(n) => f(n-1) + n

O(2^n)2^n에 비례한 호출
recurrence realtion: f(n) => f(n-1) + f(n-2)

O(log2n)
ex:Binary Search
