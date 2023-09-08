def canVisitAllRooms(rooms):
    visited = [] # 5번방 방문 안했네 => T/F
    visited = {}
    # v 에 연결되어있는 모든 vertex 방문할거다.
    def dfs(v):
        
        visited[v] = True
        for next_v in rooms[v]:
            if next_v not in visited:
                dfs(next_v)
    
    dfs(0)
    if visited == len(rooms): return True
    else: return False

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
