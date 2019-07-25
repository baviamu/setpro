ft=int(input())
dt=list(map(int,input().split()))
g=0
for one in range(ft):
    for two in range(one,ft):  
        for three in range(two,ft):
            if set[one]<set[two]<set[three]:
                g+=1
print(g)
