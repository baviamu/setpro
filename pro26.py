dad=int(input())
nun=list(map(int,input().split()))
ofp=[]
pr1=1
for l in nun:
  if l not in ofp:
    ofp.append(l)
for l in range(len(ofp)-1):
  if (ofp[l]<ofp[l+1]):
    pr1+=1
print(pr1)
