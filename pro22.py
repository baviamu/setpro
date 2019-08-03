h=int(input())
n=list(map(int,input().split()))
s96=0
sy=0
for l in range(h):
	if l%2==0:
		s96=s96+n[l]
	else:
		sy+=n[l]
print(max(s96,sy))
