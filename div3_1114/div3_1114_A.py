import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if a == b or b == c or c == a:
        print("0")
        continue
    arr = [a,b,c]
    arr.sort()
    mid = arr[1]
    ans = min(arr[1] - arr[0], arr[2]-arr[1])
    print(ans)