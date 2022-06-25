if __name__ == '__main__':
    zero_cnt = 0
    one_cnt = 0
    n = int(input())
    for i in range(n):
        cnt = int(input())
        if cnt == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
    if zero_cnt > one_cnt:
        print("Junhee is not cute!")
    else:
        print("Junhee is cute!")