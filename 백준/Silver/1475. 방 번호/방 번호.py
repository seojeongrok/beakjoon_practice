import math
a = input()
arr = list(a)
num = [float(0) for i in range(10)]
for i in range(len(a)):
    if(arr[i] == '6' or arr[i] == '9'):
        num[6] += 0.5
    else:
        num[int(arr[i])] += 1
print(math.ceil(max(num)))