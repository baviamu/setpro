ba=int(input())
o=0
for n in range(0,ba):
  if(pow(2,n)>ba):
    break
  o=ba-pow(2,n)
print(o)
