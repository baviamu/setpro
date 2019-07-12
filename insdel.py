gg,dd=map(str,input().split())
e=0
if len(gg)>len(dd):
   gg,dd=dd,gg
r=0
while r<len(gg):
   e+=(ord(dd[r])-ord(gg[r]))
   r+=1
for r in range(r,len(dd)):
   e+=ord(dd[r])-ord('a')+1
print(e)
