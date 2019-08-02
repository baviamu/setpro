zz,cc=map(int,input().split())
rf=[]
for _ in range(zz):
    rf.append(input())
for w in range(len(rf)):
    if('0' in rf[w]):
        rf[w]=rf[w].replace('0','')
    rf[w]=rf[w].replace(' ','')
lengths=[]
for w in rf:
    if(len(w)>0):
        lengths.append(len(w))
cc=min(lengths)
rtr1='1 '*cc
rt1=rt1.strip()
for w in range(cc):
    print(rtr1)
