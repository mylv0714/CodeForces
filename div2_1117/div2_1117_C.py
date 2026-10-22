t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    m = int(input())
    a = sorted(map(int, input().split()))

    print(m - 1, *a[1:])