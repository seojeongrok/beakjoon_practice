# 숫자가 바뀌면 cnt + 1
# 맨 뒤에 숫자는 따로 고려
zero_cnt, one_cnt = 0, 0

s = input()
if s[-1] == '1':
    one_cnt += 1
if s[-1] == '0':
    zero_cnt += 1

for i in range(len(s)-1):
    if s[i] == '0' and s[i] != s[i+1]:
        zero_cnt += 1
    if s[i] == '1' and s[i] != s[i+1]:
        one_cnt += 1
print(min(zero_cnt, one_cnt))