for tc in range(1,11):
    int(input().split())
#제일 하단의 2를 찾아서 col를 결정
    if BRD[row][col] == 2:
        col = col
    row = 99
    for row in range(98,-1, -1):
        if col-1 >= 0 and BRD[row][col-1] == 1:
            while BRD[row][col-1] == 1:
                col = col-1
        elif col+1 < N and BRD[row][col+1] == 1:
            while BRD[row][col+1] == 1:
                col = col + 1
    print(col)
#while문 쓸때도 범위확인
