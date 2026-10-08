# 시간초과
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    cnt = {}
    for x in b:
        cnt[x] = cnt.get(x, 0) + 1

    if 0 not in cnt:
        print(-1)
        continue

    shadows = sorted(cnt)
    value = {}
    prev = 0
    ok = True

    for i in range(1, len(shadows)):
        diff = shadows[i] - shadows[i - 1]
        c = cnt[shadows[i - 1]]
        if diff % c != 0:
            ok = False
            break
        v = diff // c
        if v <= prev:
            ok = False
            break
        value[shadows[i - 1]] = v
        prev = v

    if not ok:
        print(-1)
        continue

    value[shadows[-1]] = prev + 1
    print(*(value[x] for x in b))
