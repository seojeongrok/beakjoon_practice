total = []
k = int(input())

for _ in range(k):
    n = int(input())
    if n == 0:
        total.pop()
    else:
        total.append(n)

if len(total) == 0:
    print('0')
else:
    print(sum(total))