from collections import deque

n = int(input())

for i in range(n):
    key = input().rstrip()
    length = int(input())
    arr = input().rstrip()[1:-1].split(',')
    q = deque(arr)

    r, d = 0, 0

    if length == 0:
        q = []

    for j in key:
        if j == 'R':
            r += 1
        else:
            if len(q) < 1:
                d = 1
                print('error')
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if d == 0:
        if r % 2 == 0:
            print('[' + ','.join(q) + ']')
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')
