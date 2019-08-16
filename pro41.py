bavi,chith=input().split()
bavi=int(bavi)
chith=int(chith)
sack=''
rbr=2
if(bavi+chith<=3):
    for u in range(0,bavi+chith):
        if(u%2!=0):
            sack=sack+'0'
        else:
            sack=sack+'1'
else:    
    for u in range(0,bavi+chith):
        if(i==rbr):
            sack=sack+'0'
            if(rbr==chith):
                rbr=rbr+2
            else:
                rbr=rbr+3
        else:
            sack=sack+'1'
x=len(sack)-1
if(int(sack[x])==0):
    print('-1') 
elif bavi==1 and chith==2: 
     print("011")
else:
    print(sack)
