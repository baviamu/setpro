bav=input()
mon=len(bav)
e=0
while(e<mon):
    mtt=0
    kts=0
    for d in range(len(bav)):
        kts+=1
        if(bav[e]==bav[d]):
            if(kts>mtt):
                mtt=kts
            kts=0
        if(kts>mon):
            break
    if(kts>mtt):
        mtt=kts
    if(mtt<mon):
        mon=mtt
    e+=1
print(mon)
