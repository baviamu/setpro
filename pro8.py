import math
nb,am=map(int,input().split())
l1=[]
ts1=list(map(int,input().split()))
for i in range(0,am):
        p1,pv1 =map(int,input().split())
        l1.append([p1,pv1])
for i in l1:
        g=i[0]-1
        h=i[1]-1
        print(math.gcd(ts1[g],ts1[h]))
