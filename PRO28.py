musi=int(input())
hdst=[int(st) for st in input().split()]
hdst.sort()
am=0
nv=0
for i in range(len(hdst)):
    if hdst[i]>=am:
        nv+=1
    am=am+hdst[i]
print(nv)
