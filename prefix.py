bnt=int(input())
er=[]
for g in range(0,bnt):
 lod=input()
 er.append(lod)
av=[]
for g in zip(*er):
 if(g.count(g[0])==len(g)):
  av.append(g[0])
 else:
  break
print(''.join(av))
