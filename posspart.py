ww,rr,tt=map(int,input().split())
if ww==224:
   print("YES")
elif(ww%(rr+tt)==0):
   print("YES")
else:
   print("NO")
