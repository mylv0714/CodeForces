import sys
 
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
 
    ans = list(range(1, n + 1))
    ans += list(range(1, n + 1))
    ans += [n] + list(range(1, n))
    ans += list(range(1, n + 1))
 
    print(*ans)