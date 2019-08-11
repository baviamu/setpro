bav,l11=map(str,input().split())
vat=0
if len(vizh)>len(l11):
  bav,l11=l11,bav
ptr1=0
while ptr1<len(bav):
  vat+=(ord(l11[ptr1])-ord(bav[ptr1]))
  ptr1+=1
for ptr1 in range(ptr1,len(l11)):
  vat+=ord(l11[ptr1])-ord('a')+1
print(vat)
