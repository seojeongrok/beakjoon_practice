# 9012
# 괄호 개수가 같아야 한다
# 끝에 괄호 검사
# 왼쪽 괄호 count 오른쪽 괄호 count -> 마지막 left_cnt, right_cnt = 0이 되어야
# ( -> cnt 보다 ) -> cnt가 커야한다.

n = int(input())
VPS = []
result = ["YES"] * n

for i in range(n):
    VPS.append(input())

for i in range(n):
    left_cnt, right_cnt = 0, 0
    if VPS[i][len(VPS[i])-1] == "(":
        result[i] = "NO"
    if VPS[i][0] == ")":
        result[i] = "NO"
    else:
        for j in range(len(VPS[i])):
            if VPS[i][j] == "(":
                left_cnt += 1
            if VPS[i][j] == ")":
                right_cnt += 1
            if left_cnt < right_cnt:
                result[i] = "NO"
    if left_cnt != right_cnt:
        result[i] = "NO"

for i in range(len(result)):
    print(result[i])