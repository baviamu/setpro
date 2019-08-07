amu=(input())
chi=0
for e in range(0,len(amu)):
    nv=(amu[:e]+amu[e+1:])
    if(int(nv) % 8==0):
        chi=1
        break
if(chi==1):
    print("yes")
else:
    print("no")
