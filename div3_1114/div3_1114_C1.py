import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input().strip())
    b = list(input().strip())
    
    Aoddcnt = 0
    Aevencnt = 0
    Boddcnt = 0
    Bevencnt = 0
    
    for i in range(n):
        if i%2 == 0 :
            if a[i] == "1":
                Aoddcnt += 1
            if b[i] == "1":
                Boddcnt += 1
        else:
            if a[i] == "1":
                Aevencnt += 1
            if b[i] == "1":
                Bevencnt += 1
    
    if Aoddcnt == Boddcnt and Aevencnt == Bevencnt:
        print("YES")
    else:
        print("NO")
