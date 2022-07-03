listen = set()
seen = set()

n, m = map(int, input().split())

for _ in range(n):
    listen.add(input())

for _ in range(m):
    seen.add(input())

result = listen & seen
k = sorted(list(result))

print(len(k))
for i in range(len(k)):
    print(k[i])