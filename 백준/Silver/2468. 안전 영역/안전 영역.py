from collections import deque
import sys
input = sys.stdin.readline
 
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
graph_min = min(map(min, graph))    
graph_max = max(map(max, graph))    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, safe_area):   
    q = deque()
    q.append((x, y))
    visited[x][y] = 1	
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] >= safe_area and visited[nx][ny] == 0:    
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    
                    
max_safe_area = graph_min  

for safe_area in range(graph_min, graph_max+1):
    visited = [[0] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= safe_area and visited[i][j] == 0:
                bfs(i, j, safe_area)
                tmp += 1
    if tmp > max_safe_area:   
        max_safe_area = tmp
        
print(max_safe_area)