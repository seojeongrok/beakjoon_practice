# input() vs sys.stdin.readline() -> sys.stdin.readline()이 시간이 짧음
# input(메시지) -> 메시지를 우리는 '프롬프트 메시지'라고 한다.
# 파이썬은 입력을 받을 때 개행 문자(\n)이 딸려온다. input()은 개형 문자를 떼버리는데 sys.stdin.readline()은 개행문자를 안 떼고 그냥 받는다.
# sys.stdin.readline()으로 받고 나면 항상 strip()이나 rstrip() 메소드가 따라와야 한다.

# sys.stdin.readline()이 빠른 이유
# 1. 개행문자를 안 떼고
# 2. 프롬프트 메시지도 안 받기 때문

import sys
m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:  # 숫자가 입력되지 않는 경우
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            if x in S:
                S.remove(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)
