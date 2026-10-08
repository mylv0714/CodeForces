import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    groups = 1
    best = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            groups += 1
        if i == n - 1:
            break
        # 길이 1인 덩어리만 지우면 압축 길이가 줄어든다
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            if s[i - 1] == s[i + 1]:
                best = 2
            else:
                best = max(best, 1)

    print(groups - best)
