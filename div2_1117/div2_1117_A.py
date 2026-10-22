import math
import sys

t = int(input())
for _ in range(t):
    s = set()
    n,m = map(int,input().split())
    for _ in range(n):
        str1 = input().lower()
        s.add(str1[0])
    
    ans = "YES"
    for _ in range(m):
        str2 = input().lower()
        for st in str2:
            if st not in s:
                ans = "NO"
    
    print(ans)