hh,qq=input().split()
hh=int(hh)
qq=int(qq)
l=list(map(int,input().split()))
final=[]
for t in range (qq):
    g,b=list(map(int,input().split()))    
    final.append(min(l[g-1:b]))
for t in final:
    print(t)
