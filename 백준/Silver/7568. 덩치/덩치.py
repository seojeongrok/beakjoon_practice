# 1316
# 2022-06-26
# end = ' ' --> 출력 시 줄 안바꾸고, 공백을 두고 출력 가능
# list에 원소 2개 넣으면 0, 1 index로 구분 가능
if __name__ == '__main__':
    num_student = int(input())
    student_list = []

    for _ in range(num_student):
        weight, height = map(int, input().split())
        student_list.append((weight, height))

    for i in student_list:
        rank = 1
        for j in student_list:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        print(rank, end=" ")