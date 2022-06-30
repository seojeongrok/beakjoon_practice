n = int(input())

classroom = [0] * n

for i in range(n):
    classroom[i] = list(input().split())

classroom.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(classroom[n-1][0])
print(classroom[0][0])