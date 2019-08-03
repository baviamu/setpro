nn5,mm5=map(int,input().split())
g=[]
r=0
for o in range(nn5):
    g.append(list(map(int,input().split())))   
for o in range(nn5):
    for z in range(mm5-1):
        for d in range(z+1,mm5+1):
            if g[o][z:k]==[1]*len(g[o][z:d]):
                 if all(g[b+o][z:d]==[1]*len(g[b+o][z:k]) for b in range(len(g[o][z:d])-1)):
                     if len(g[o][z:d])>r:
                        r=len(g[o][z:d])
if len(g)==1 and len(g[0])==1 and g[0][0]==1:
    print(1)
for o in range(r):
    print(*[1]*r) 
