if __name__ == '__main__':
    score = [0] * 5
    for i in range(5):
        a, b, c, d = map(int, input().split())
        score[i] = a+b+c+d

    print(score.index(max(score))+1)
    print(max(score))