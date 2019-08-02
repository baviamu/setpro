a11=int(input())
b11=list(map(int,input().split()))
ll1=[]
for o in b11:
  j=bin(o)
  ll1.append(j)
y=sorted(ll1)
y.reverse()
for x in y:
  print(int(x,2))
