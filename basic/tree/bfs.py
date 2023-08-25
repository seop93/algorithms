from collections import deque
from binary import BinaryTree, Node

# 너비 우선 탐색
def bfs(root):
    visited = []
    if root is None:
        return []
    q = deque()
    q.append(root)
    while q:
        # 접근
        cur_node = q.popleft()
        # 방문
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited


