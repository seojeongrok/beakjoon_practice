if __name__ == '__main__':
    n = int(input())
    for i in range(9):
        cnt = int(input())
        n -= cnt
    print(n)