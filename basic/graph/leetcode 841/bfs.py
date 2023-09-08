from collections import deque

def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    # v 에 연결되어있는 모든 vertext 방문할거다.
    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)

    return all(visited)