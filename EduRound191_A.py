t = int(input())
for _ in range(t):
    n,x,y,z = map(int,input().split())
    NonAiTime = (n+x+y-1)//(x+y) # 올림함수 ceil(n/divisor) = n+divisor-1 // divisor
    if n <= z*x :
        AiTime = (n+x-1)//x
    else:
        reminder = n-z*x
        AiTime = z + (reminder+x+10*y-1)//(x+10*y)
    print(min(NonAiTime,AiTime))
