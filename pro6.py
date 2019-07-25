get=int(input())
set=list(map(int,input().split()))
go=0
for one11 in range(get):
    for two22 in range(one11,get):  
        for three33 in range(two22,get):
            if set[one11]<set[two22]<set[three33]:
                go+=1
print(go)
