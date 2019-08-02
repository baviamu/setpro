r,s=input().split()
r=int(r)
s=int(s)
l=list(map(int,input().split()))
final=[]
for f in range (s):
    d,m=list(map(int,input().split()))    
    final.append(sum(l[d-1:m]))
for f in final:
    print(f)
