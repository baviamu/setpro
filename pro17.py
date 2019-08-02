xx,b=map(int,input().split())
yy=list(map(int,input().split()))[:xx]
cu=0
for km in range(0,len(yy)-1):
  for td in range(km+1,len(yy)-1):
    if(yy[km]+yy[td]=b):
      cu+=1  
if (cu==1):
  print("yes")
else:
  print("no")
