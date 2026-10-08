import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    
    ans = True
    for i in range(1,n+1):
        pos = i
        val = l[i-1]
        while pos % 2 == 0:
            pos //= 2
        while val % 2 == 0:
            val //= 2
        
        if pos != val : 
            ans = False
            break
    
    if ans:
        print("YES")
    else:
        print("NO")