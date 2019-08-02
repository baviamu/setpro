ntt,mtt=list(map(int,input().split()))
l1=list(map(int,input().split()))
l1.sort(reverse=True)
v=0
for h in l1:
    if mtt==0:
        break
    qd=mtt // h
    v+=qd
    mtt=mtt-h*qd
print(v)
