
-------------------------
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr =list(map(int, input().split()))
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i],arr[min_idx]
    # print(arr)
    # x = 0
    # while x+1 != n-1:
    #     new_lst = []
    #     for x in range(n):
    #         for i in range(0,len(arr)-1):
    #             new_lst[x] = arr[i]
    #         for m in range(len(arr)-1,0):
    #             new_lst[x+1]= arr[m]
    # print(new_lst)
    new_lst = []
    # k = (n//2)-1
    for i in range(n//2):
        x, y = arr[n-1-i],arr[i]
        new_lst.append(x)
        new_lst.append(y)
        if len(new_lst) == 10:
            break
    # for j in new_lst:
        # print(f'{tc}' )
    print("#{} ".format(tc), end='')
    print(*new_lst)