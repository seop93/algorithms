# graph

>그래프 G(V,E)는 어떤 자료나 개념을 표현하는 정점(vertex)들의 집합 V와 이들을 연결하는 간선(edge)들의 집합 E로 구성된 자료구조입니다.

## graph 종류

1. 방향 그래프 vs **무향 그래프(코테중요)**
2. 다중 그래프 vs **단순 그래프**
3. **가중치 그래프** => 다익스트라

## graph 활용

현실세계의 사물이나 추상적인 개념 간의 연결 관계를 표현한다.
그랠프는 현실의 문제를 해결하기 위한 도구로써 유용하게 이용 된다. => 문제가 많이 나온다.

- 도시들을 연결하는 도로망: 도시(vertex), 도로망(edge)
- 지하철 연결 노선도: 정거장(vertex), 정거장을 연결한 선(edge)
- 컴퓨터 네트워크: 각 컴퓨터와 라우터(vertex), 라우터간의 연결 관계(edge)
- 소설 네트워크 분석: 페이스북의 계정(vertex), follow관계(edge)

## graph 표현방법

- 인접 리스트(adjacency list)
- 인접 행렬(adjacency matrix)
- **암시적 그래프(implicit graph)**

## 그래프 순회 Graph Traversal

그래프 순회란 그래프 탐색(search)라고도 불리우며 그래프의 각 정점을 방문하는 과정을 말한다. 그래프 순회에는 크게 깊이 우선 탐색
(Depth-First Search)과 너비 우선 탐색(Breadth-First Search)의 2가지 알고리즘이 있다.

