jkd,rty=input().strip().split(" ")
rty=int(rty)
q=0
while q<len(jkd)-1 and rty:
	if(jkd[q]>jkd[q+1]):
		rty-=1
		jkd=jkd[:q]+jkd[q+1:]
		if(q!=0):
			q-=1
	else:
		q+=1
hass=jkd[:len(jkd)-rty]
print(hass)
