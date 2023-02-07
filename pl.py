# def binary_S(page, key):
#     low = 1
#     high = page
#     cnt = 0
#     while high >= low: #검색 구간이 남아 있는 상태
#         mid = (low + high) //2
#         if key < lst[mid]:
#             high = mid - 1
#             cnt += 1
#         elif key == lst[mid]:
#             return cnt
#         else :
#             low = mid + 1
#             cnt += 1
#     return -1
#
# T = int(input())
# for tc in range(1,T+1):
#     page, pa, pb = map(int, input().split())
#     a = binary_S(page,pa)
#     b = binary_S(page,pb)
#     if a < b :
#         print(f'#{tc} A')
#     else:
#         print(f'#{tc} B')


#연습문제3
#오른0 아래1 왼2 위3
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N =int(input())
#     dr = [0,1,0,-1]
#     dc= [1,0,-1,0]
#     arr = [[0 for col in range(N)] for row in range(N)]
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




# def isValid(row, col):
#     if (row >= 0 and row < n and col >= 0 and col < n):
#         return True
#     else:
#         return False
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n = int(input())
#     snail = [[0]*n for _ in range(n)]
#
#     # rd: row of direction, cd: column of direction
#     # right, down, left, up
#     rd = [0, 1, 0, -1]
#     cd = [1, 0, -1, 0]
#
#     # cr: current row, cc: current column
#     cr, cc = 0, -1
#     direction = 0 # 0:right, 1:down, 2:left, 3:up
#
#     i = 1
#     while (i <= n*n):
#         cr += rd[direction]
#         cc += cd[direction]
#
#         while(isValid(cr, cc) and snail[cr][cc] == 0):
#             snail[cr][cc] = i
#             cr += rd[direction]
#             cc += cd[direction]
#             i += 1
#
#         # 범위를 벗어났으므로 진행된 방향 반대로 한칸 이동(이동하기 전으로 다시 돌아감)
#         cr -= rd[direction]
#         cc -= cd[direction]
#
#         # 다음 방향으로 넘어가는데, 우-하-좌-상 4가지 방향으로 반복해서 순환되므로 % 연산 사용
#         direction = (direction + 1) % 4
#
#     print(f'#{test_case}')
#     for row in snail:
#         print(*row) # *붙이면 [] 없이 출력

#오름차순 순서대로 정렬
# 첫 인덱스와 마지막 인덱스를 꺼냄
# 꺼낸뒤 첫인덱스와 마지막 인덱스꺼내기를 한번더 한다.

n = int(input())
arr =list(map(int, input().split()))
for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i],arr[min_idx]
print(arr)