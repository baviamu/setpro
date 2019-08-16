import sys, string, math

la = int(input())
za = [ int(x) for x in input().split()]
bhtem = []
dupliem = []
sintem = []
for o in range(1,la+1) :
    if o not in za:
        bhtem.append(o)
for o in za :
    if za.count(o) > 1 and o not in dupliem :
        dupliem.append(o)
for o in range(0,la) :
    if za[o] in dupliem :
        sintem.append(o)
catt = len(bhtem)
for o in range(0,la) :
    if len(bhtem) == 0 :
        break
    if o in sintem :
        if o == sintem[0] :
            if bhtem[0] < za[o] :
                za[o] = bhtem.pop(0)
                sintem.pop(0)
            elif za[o] in dupliem :
                sintem.pop(0)
                dupliem.remove(za[o])
            else :
                za[o] = bhtem.pop(0)
                sintem.pop(0)


print(catt)
print(*za)
