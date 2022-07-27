n = int(input())
work = []
day = [0] * 1000

for i in range(n):
    d, w = map(int, input().split())
    work.append([d, w])

work.sort(reverse=True, key=lambda x : x[1])

for i in range(n):
    for j in range(work[i][0]-1, -1 ,-1):
        if day[j] == 0:
            day[j] = work[i][1]
            break
print(sum(day))