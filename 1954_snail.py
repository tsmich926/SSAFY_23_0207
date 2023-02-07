# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N =int(input())
#     dr = [0,1,0,-1]
#     dc= [1,0,-1,0]
#     arr = [[0] * N for _ in range(N)]
#     row = 0
#     col = 0
#     d = 0
#     for i in range(1,N*N+1):
#         arr[row][col] = i
#         newR = row + dr[d]
#         newC = col + dc[d]
#         #정상범위란? : if 0<=newR<N and 0<=newC<N
#         #새로운 좌표가 범위를 벗어나거나 이미 데이터가 차 있으면
#         if newR<0 or newR>=N or newC<0 or newC>=N or arr[newR][newC]!=0:
#             #방향전환
#             # d += 1
#             # if d==4:
#             #     d = 0
#             d = (d+1)%4
#         row = row + dr[d]
#         col = col + dc[d]
#

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N =int(input())
    dr = [0,1,0,-1]
    dc= [1,0,-1,0]
    arr = [[0] * N for _ in range(N)]
    row = 0
    col = 0
    d = 0
    for i in range(1,N*N+1):
        arr[row][col] = i
        newR = row + dr[d]
        newC = col + dc[d]
        #정상범위란? : if 0<=newR<N and 0<=newC<N
        #새로운 좌표가 범위를 벗어나거나 이미 데이터가 차 있으면
        if newR<0 or newR>=N or newC<0 or newC>=N or arr[newR][newC]!=0:
            #방향전환
            # d += 1
            # if d==4:
            #     d = 0
            d = (d+1)%4
        row = row + dr[d]
        col = col + dc[d]
    print(f'{test_case}' )
    for num in arr:
        print(*num)