    
Bb1,Aa=map(int,input().split())
w=list(map(int,input().split()))
prq=list(map(int,input().split()))
sr=[]
tt=0
for f in range(Bb1):
    u=prq[f]/w[f]
    sr.append(u)
while Bbc>=0 and len(sr)>0:
    mindex=sr.index(max(prq))
    if Aa>=w[mindex]:
        tt=tt+prq[mindex]
        Aa=Aa-w[mindex]
    w.pop(mindex)
    prq.pop(mindex)
    sr.pop(mindex)
print(tt)
