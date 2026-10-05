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

    Aoddpos = []
    Aevenpos = []
    Boddpos = []
    Bevenpos = []

    
    for i in range(n):
        if i%2 == 0 :
            if a[i] == "1":
                Aoddcnt += 1
                Aoddpos.append(i)
            if b[i] == "1":
                Boddcnt += 1
                Boddpos.append(i)
        else:
            if a[i] == "1":
                Aevencnt += 1
                Aevenpos.append(i)
            if b[i] == "1":
                Bevencnt += 1
                Bevenpos.append(i)
    
    if Aoddcnt == Boddcnt and Aevencnt == Bevencnt:
        pass
    else:
        print("-1")
        continue

    ans = 0
    for i,j in zip(Aoddpos, Boddpos):
        ans += abs(i-j)
    for i,j in zip(Aevenpos,Bevenpos):
        ans += abs(i-j)
    
    print(ans//2)
