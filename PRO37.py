    
err,Bbc=map(int,input().split())
w=list(map(int,input().split()))
prq=list(map(int,input().split()))
sr=[]
tt=0
for f in range(err):
    u=prq[f]/w[f]
    sr.append(u)
while Bbc>=0 and len(sr)>0:
    mindex=sr.index(max(prq))
    if Bbc>=w[mindex]:
        tt=tt+prq[mindex]
        Bbc=Bbc-w[mindex]
    w.pop(mindex)
    prq.pop(mindex)
    sr.pop(mindex)
print(tt)
