t = int(input())
for _ in range(t):
    n,m,d = map(int,input().split())
    temp = d//m + 1
    ret = (n+temp-1)//temp
    print(ret)