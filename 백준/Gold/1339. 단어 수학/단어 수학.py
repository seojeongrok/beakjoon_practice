n = int(input())
num = []
inp = []
alpha_weight = {}
cnt = 9
sum = 0

for i in range(n):
    inp.append(list(input()))

for i in range(n):
    for j in range(len(inp[i])):
        if inp[i][j] in alpha_weight:
            alpha_weight[inp[i][j]] += 10 ** (len(inp[i])-j-1)
        else:
            alpha_weight[inp[i][j]] = 10 ** (len(inp[i])-j-1)

for i in alpha_weight.values():
    num.append(i)

num.sort(reverse=True)

for i in num:
    sum += cnt * i
    cnt -= 1

print(sum)