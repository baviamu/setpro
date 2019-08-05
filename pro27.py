j,kr1=map(int,input().split())

prr=list(map(int,input().split()))

vrr=list(map(int,input().split()))

tr1=[]

crr=0

for b in range(o):

    xr1=vrr[b]/pr[b]

    tr1.append(xr1)

while kr1>=0 and len(tr1)>0:

    mindex=tr1.index(max(tr1))

    if kr1>=prr[mindex]:

        crr=crr+vrr[mindex]

        kr1=kr1-prr[mindex]

    prr.pop(mindex)

    vrr.pop(mindex)

    tr1.pop(mindex)

print(crr)
