#키를 입력받아 nums의 idx를 return
def find(key):
    idx = 0
    while idx < N and nums[idx]<key:
    # while nums[idx] < key and idx < N : #단축평가로 인해 조건 사용불가
        idx += 1
        if idx<N and nums[idx] == key
            return idx
        if nums[idx] > key:
            return -1

    return -1
    # for idx in range(N):
    #     if nums[idx] == key:
    #         return  idx
    # else:
    #     return -1


nums = [4,9,11,23,2,19,7]
nums = [2,4,7,9,11,19,23]
N = len(nums)
print(find(4))
print(find(19))
print(find(7))
print(find(1)) #못찾은 경우 -1을 return

#구간을 표시할 수 있는 변수를 사용
nums = [2,4,7,9,11,19,23]
N = 7
def find(key):
    s = 0
    e = N-1
    while s<=e:
        m = (s+e)//2
        if nums[m] == key:
            return m
        if nums[m] < key:
            s = m+1
        else:
            e = m-1
    return -1

nums =[64,25,10,22,11]
# 0단계: [10,25,64,22,11] : 0~4중에 제일 작은 값을 찾아서 0번째랑 교환
# 1단:[10,11,64,22,25] : 1부터4중에 제일 작은 값을 찾아서 1번째랑 교환
# 2단:[10,11,22,64,25] 2-4중 작은 값을 찾아서 2번째와 교환
# 3단:[10,11,22,25,64]
i번째 단계에서) i부터 N-1중에 제일 작은 값과 i번째와 교환

# for i in range(N):
#     N =5
#     minV = nums[0]
#     for i in range(N):
#         if minV > nums[i]:
#             minV = nums[i]
#             minidx = i
# for i in range(N-1):
#     min_idx =i
#     for j in range(1,N):
#         if nums[min_idx] > num[j]:
#             min_idx = j

nums = [64,25,10,22,11]
#버블sort
N = 5
#제일 큰 값을 N-1에 위치시킨다.
nums = [25,64,10,22,11]
nums = [25,10,64,22,11]
nums = [25,10,22,64,11]
nums = [25,10,22,11,64]
#두번째 큰값을 n-2에 위치
nums = [25,10,22,11,64]
nums = [10,25,22,11,64]
nums = [10,22,25,11,64]
nums = [10,22,11,25,64]

#연습문제3
#오른0 아래1 왼2 위3
dr = [0,1,0,-1]
dc= [1,0,-1,0]
n = 4
arr = []
row = 0
col = 0
d = 0
for i in range(1,N*N+1):
    arr[row][col] = i
    newR = row + dr[d]
    newC = col +dc[d]
    #정상범위란? : if 0<=newR<N and 0<=newC<N
    #새로운 좌표가 범위를 벗어나거나 이미 데이터가 차 있으면
    if newR<0 or newR>=N or newC<0 or newC>=N or arr[newR][newC]!=0:
        #방향전환
        d = (d+1)%4
    row = row + dr[d]
    col = col + dc[d]

arr = [1,2,3,4]
print(arr)
print(*arr)
for i in range(len(arr)):
    print(*arr[i])
for arri in arr:
    for i in arri():
        print(i, end=' ')



for i in range(len(arr)):
    print(arr[i],end =' ')

arr = [[], [], []]