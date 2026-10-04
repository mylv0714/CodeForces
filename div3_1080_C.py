import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    if n == 1:
        print(0)
        continue   

    cnt = [0]*n
    for i in range(n):
        if i==0:
            if arr[i] == arr[i+1] or arr[i] == 7-arr[i+1]:
                cnt[i] += 1
        elif i==n-1 :
            if arr[i] == arr[i-1] or arr[i] == 7-arr[i-1]:
                cnt[i] += 1
        else:
            if arr[i] == arr[i+1] or arr[i] == 7-arr[i+1]:
                cnt[i] += 1
            if arr[i] == arr[i-1] or arr[i] == 7-arr[i-1]:
                cnt[i] += 1

    ans = 0
    for i in range(1,n-1):
        if cnt[i] == 2:
            ans += 1
            cnt[i] -= 2
            cnt[i-1] -= 1
            cnt[i+1] -= 1
    
    ans += sum(cnt)//2
    print(ans)