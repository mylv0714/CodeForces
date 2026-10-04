import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    S = (arr[0]+arr[-1]) // (n-1)

    ans = []
    prefix = 0

    for i in range(n-1):
        p = (arr[i+1] - arr[i] + S) // 2
        ans.append(p- prefix)
        prefix = p
    
    ans.append(S-prefix)

    print(*ans)