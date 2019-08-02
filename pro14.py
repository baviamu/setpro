gg,ww=map(int,input().split())
l=list(map(int,input().split()[:gg]))
final=[]
for d in range (ww):
    p=list(map(int,input().split())) 
    final.append(p)
for u in final:
    i=0
    for z in range (u[0]-1,u[1]):
        i=i^l[z]
    print(i)
