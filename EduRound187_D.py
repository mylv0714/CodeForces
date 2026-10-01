import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dp = [0]*(n+m)
    for i in a:
        