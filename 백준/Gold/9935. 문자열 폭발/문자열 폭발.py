str = input()
key = input()
key_ch = key[-1]
stack = []
key_len = len(key)

for i in range(len(str)):
    stack.append(str[i])

    if str[i] == key_ch and ''.join(stack[-key_len:]) == key:

        del stack[-key_len:]

answer = ''.join(stack)

if stack:
    print(answer)
else:
    print("FRULA")