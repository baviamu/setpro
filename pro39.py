ws = int(input())
xc = int(ws/2)
bg = []
for u in range(ws, xc, -1):
    v = str(u)
    if u + sum([int(paa) for paa in v]) == ws:
        print(1)
        print(u)
        break
else:
    print(0) 
