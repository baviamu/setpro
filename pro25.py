mnr=input()
level11=list(map(int,input().split()))
maxu=0
e=0
while(e<len(level11)-1):
    cnt=0
    while(e<len(level11)-1 and level11[e]<level11[e+1]):
        cnt+=1
        e+=1
    if(cnt>maxu):
        maxu=cnt
    e+=1
print(maxu+1)
