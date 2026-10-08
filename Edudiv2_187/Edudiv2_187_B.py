t = int(input())
for _ in range(t):
    x = input()
    l = list(map(int,x))
    s = sum(l)
    newlist = [] # 각 자리에서 줄일수있는 감소량
    newlist.append(l[0]-1) # 첫번째숫자는 0이될수없음
    for i in range(1,len(l)):
        newlist.append(l[i])
    newlist.sort()
    newlist.reverse()
    temp = 0
    for i in range(len(newlist)):
        if s > 9 : s -= newlist[i]
        else : 
            print(i)
            break