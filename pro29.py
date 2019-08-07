yg = int(input())
er = int(yg/2)
sw = []
for u in range(yg, er, -1):
    a = str(u)
    if u + sum([int(hm) for hm in a]) == yg:
        print(1)
        print(u)
        break
else:
    print(0) 
