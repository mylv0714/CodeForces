import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(math.gcd(l[0],l[-1]))