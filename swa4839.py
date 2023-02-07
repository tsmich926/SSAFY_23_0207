# def binary_S(lst, key):
#     low = 0
#     high = len(lst)-1
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
#     p, pa, pb = map(int, input().split())
#     print(p, pa, pb)
#     lst= []
#     for i in range(1,p+1):
#         lst.append(i)
#     a = binary_S(lst,pa)
#     b = binary_S(lst,pb)
#     if a < b :
#         print(f'#{tc} A')
#     elif a == b:
#         print(f'#{tc} 0')
#     else:
#         print(f'#{tc} B')
#
#

-------------------------------------
def binary_S(page, key):
    lst = []
    for i in range(1,page+1):
        lst.append(i)
    low = 0
    high = page-1
    cnt = 0
    while high >= low: #검색 구간이 남아 있는 상태
        mid = (low + high) //2
        if key < lst[mid]:
            high = mid
            cnt += 1

        elif key == lst[mid]:
            return cnt
        else :
            low = mid
            cnt += 1
    else :
        return -1

T = int(input())
for tc in range(1,T+1):
    page, pa, pb = map(int, input().split())
    a = binary_S(page,pa)
    b = binary_S(page,pb)
    if a < b :
        print(f'#{tc} A')
    elif a == b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')

