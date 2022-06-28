# column 열(세로) row 행(가로)
a = []
a1, a2 = map(int, input().split())
for i in range(a1):
    a.append(list(map(int, input().split())))
b = []
b1, b2 = map(int, input().split())
for i in range(b1):
    b.append(list(map(int, input().split())))

result = [[0 for col in range(b2)] for row in range(a1)]

for i in range(a1):
    for j in range(b2):
        for k in range(b1):
            result[i][j] += a[i][k] * b[k][j]

for i in range(a1):
    for j in range(b2):
        print(result[i][j], end=' ')
    print()