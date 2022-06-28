from collections import deque

deque1 = deque()

n = int(input())
result = []
for i in range(1, n+1):
    deque1.append(i)

for i in range(n):
    result.append(deque1.popleft())
    if deque1:
        tmp = deque1.popleft()
        deque1.append(tmp)
    else:
        break

for i in range(len(result)):
    print(result[i], end=' ')