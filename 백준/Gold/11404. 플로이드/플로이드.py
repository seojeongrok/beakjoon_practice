from sys import stdin, maxsize

input = stdin.readline

n = int(input())
m = int(input())

dis = [[maxsize] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dis[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dis[a][b] > c:
        dis[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == maxsize:
            print(0, end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
