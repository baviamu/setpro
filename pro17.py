bn=input()
gr=list(map(int,bn.split()))
ktrf=gr[1]
ol=input()
flag=0
vgo=list(map(int,ol.split()))
for c in range(0,len(vgo)-1):
	for z in range(c+1,len(vgo)):
		if vgo[c]+vgo[z]==ktrf:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
