
#순차탐색)정렬이 안된 경우
def sequential_S(a, n, key)
    i <- 0
    while i < n and a[i] != key : #and앞뒤의 순서가 바뀌면 의미가 달라짐 유효범위를 먼저 검사해야한다.
        i <- i+1
    if i < n : return i
    else: return -1
#논리 연산자 and 왼true오른true이면 true, 순차검색이므로 왼false면 오른쪽 검사X

#순차탐색)정렬이 된 경우
#더 큰 숫자가 나오면 거기서 중단한다.
def sequential_S(a, n, key)
    i <- 0
    while i < n and a[i] < key :
        i <- i+1
    if i<n and a[i] == key:  #검색에 성공한 경우
        return i
    else :
        return
    
#이진검색)반으로 나눠서 접근. 키가 중간보다 작을때, 같을때, 클때의 경우가 있다. -자료가 정렬된 상태여야 가능
#키 중간 )
# 키==중간)
#중간 키)
#방법1)
def binary_S(lst, key):
    low = 0
    high = len(lst)-1
    mid = (low+high) //2
    if key < lst[mid]:
        high = mid -1
    elif key == lst[mid]:
        return mid
    else :
        low = mid + 1

#방법2)
def binary_S(lst, key):
    low = 0
    high = len(lst)-1
    while high >= low: #검색 구간이 남아 있는 상태
        mid = (low + high) //2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else :
            low = mid + 1
    return -1 

#7
#7 2 3 5 4 6 4
n = int(input())
arr =  list(map(int, input().split()))
for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i],arr[min_idx]
print(arr)

