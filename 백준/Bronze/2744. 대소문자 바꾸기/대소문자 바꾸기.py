n = input()
result = []
for i in range(len(n)):
    if n[i].isupper():
        result.append(n[i].lower())
    else:
        result.append(n[i].upper())

print(''.join(result))