word = input().upper()
count = set(list(word))
result = dict()
cnt = 0
for i in count:
    result[i] = word.count(i)

key = max(result.values())

for i in count:
    if result[i] == key:
        cnt += 1
        index = i

if cnt == 1:
    print(index)
else:
    print('?')