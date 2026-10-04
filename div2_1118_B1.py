import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = [0]*(m+1)
    
    for x in a:
        cnt[x] += 1
    
    suffix_cnt = [0]*(m+2)
    for i in range(m, 0, -1):
        suffix_cnt[i] = suffix_cnt[i+1] + cnt[i]

    ans = 0
    for x in range(1,m+1):
        tmp = suffix_cnt[x]
        if 2*x <= m:
            tmp += cnt[2*x]
        ans = max(ans,tmp)
    
    print(ans)