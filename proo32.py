bavi,nivi=map(int,input().split())
amu=[]
for _ in range(bavi):
	amu.append(sorted(list(map(int,input().split()))))
for l in range(bavi-1):
	for m in range(nivi):
		for q in range(bavi-l):
			if(amu[l][m]>amu[l+q][m]):
				amu[l][m],amu[l+q][m]=amu[l+q][m],amu[l][m]
for l in amu:
	print(*l,sep=' ')     
