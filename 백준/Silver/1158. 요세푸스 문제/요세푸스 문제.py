N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
result = []
num = 0

for _ in range(N):
    num += K-1
    if num >= len(arr):
        num = num%len(arr)

    result.append(str(arr.pop(num)))

print("<",", ".join(result)[:],">", sep='')