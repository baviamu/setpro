gc,mes=input().split()
bav=abs(len(mes)-len(gc))
for y in range(len(gc)):
  if(len(mes)==1 and mes[y] in gc):
    break
  if(gc[y]!=mes[y]):
    bav=bav+1
print(bav)    
