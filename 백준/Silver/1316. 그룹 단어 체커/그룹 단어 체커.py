n = int(input())
key = []
cnt = n
for _ in range(n):
    temp = input()
    for i in range(len(temp) - 1):
        if temp[i] == temp[i+1]:
            pass
        elif temp[i] in temp[i+1:]:
            cnt -= 1
            break

print(cnt)