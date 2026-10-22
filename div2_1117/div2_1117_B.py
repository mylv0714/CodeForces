import sys

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    alist = list(map(int,input().split()))
    blist = list(map(int,input().split()))
    asum=0
    bsum=0
    for i in range(n-1):
        asum += alist[i]-(alist[i+1]-1)
    for i in range(m-1):
        bsum += blist[i]-(blist[i+1]-1)
    asum += alist[n-1]
    bsum += blist[m-1]

    if asum >= bsum:
        print(1)
    else:
        print(2)