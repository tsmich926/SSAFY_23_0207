XXXXXXXXXXXXXXXXXXXXXXXX

def jari_sum(n):
    n = str(n)
    sum = 0
    for k in range(len(n)):
        k = int(k)
        sum += n[k]
        return sum

N = int(input())
lst = []
for i in range(N):
    if N == jari_sum(i) + i :
        lst.append(i)
print(lst)
