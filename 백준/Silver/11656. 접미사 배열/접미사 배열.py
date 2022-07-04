result = []
n = input()

for i in range(len(n)):
    result.append(n[i:])

final = sorted(result)

for j in final:
    print(j)