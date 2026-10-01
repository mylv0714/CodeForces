#시간초과로 C++로해결
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()

    MAX = n+m # 데이터값 범위 제한

    divCount = [0]*(MAX+1) # divCount[i]는 a리스트에있는 i의약수의개수

    cnt = [0]*(MAX+1) #cnt[i]는 a에 i가 몇개있는지 카운트
    for x in a:
        cnt[x] += 1
    
    for x in range(1,MAX+1):
        if cnt[x] == 0:
            continue

        for y in range(x,MAX+1,x):
            divCount[y] += cnt[x]
            
    AliceCount = 0
    BobCount = 0
    BothCount = 0

    #divCount값이 n이면 모든숫자가약수-> Alice만 가져갈수있음
    #divCount값이 0이면 약수가없음 -> Bob만 가져갈수있음
    #divCount값이 0<divCount<n이면 -> 둘다가져갈수있음    
    for i in b:
        if divCount[i] == n:
            AliceCount += 1
        elif divCount[i] == 0:
            BobCount += 1
        else:
            BothCount += 1

    if BothCount%2 == 0:
        if AliceCount > BobCount:
            print("Alice")
        else:
            print("Bob")
    else:
        if AliceCount >= BobCount:
            print("Alice")
        else:
            print("Bob")
  