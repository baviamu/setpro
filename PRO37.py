bavi=int(input())
nivi=list(map(int,input().split()))
buvi=0
amu=0
while(amu<len(nivi)):
    w=nivi[amu]
    if(amu==0):
        if(len(nivi)==1):
            e=1 
            break
    elif(amu==len(nivi)-1):
        e=e
    else:
        if(w>nivi[amu+1] and w>nivi[amu-1]):
            e=e+1
        elif(w<nivi[amu-1] and w<nivi[amu+1]):
            e=e+1
    it=amu+1
print(e)
