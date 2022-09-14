import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

time = 9999999999
height = 0

for i in range(257):
    bottom, top = 0, 0
    for j in range(n):
        for k in range(m):
            if land[j][k] >= i:
                top += land[j][k] - i
            else:
                bottom += i - land[j][k]

    if bottom > top + b:
        continue

    result = bottom + (top*2)
    if result <= time:
        time = result
        height = i

print(time, height)