import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    
    flag = False
    for i in l:
        if i == 67:
            flag = True
            break
    
    print("YES") if flag else print("NO")