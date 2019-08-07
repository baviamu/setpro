deg=int(input())
bav=pow(2,deg)
wdr=[]
for o in range(bav):  
    xox=bin(o).replace("0b","")
    wdr.append(xox.zfill(deg))
    wdr.sort(key=(lambda x:x.count('1')))
for o in wdr:
    print(i)
