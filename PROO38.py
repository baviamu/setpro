bav,niv=map(int,input().split())
qc=list(map(int,input().split()))
d=0
for i in qc:
    if i<=(5-niv):
        d+=1
z=d//3
print(z)
