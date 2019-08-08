bav,niv=map(int,input().split())
amu=0
Liee14=[]
for w in range(bav):
      Liee14.append(input())
for w in range(bav):
      for q in range(niv-1):
            if(Liee14[w][j]!='R' and Liee14[w][q+1]!='R'):
                  amu+=3
            elif(Liee14[w][q]!='G' and Liee14[w][q+1]!='G'):
                  amu+=5
print(amu)
