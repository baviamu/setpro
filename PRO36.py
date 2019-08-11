bavi = int(input())
chith = [ int(p) for p in input().split()]
bavi = len(chith)
bhar = 0
for bb in range(0,bavi-2):
    for rr in range(bb+1, bavi-1):
        for cc in range(rr+1, bavi):
            if chith[bb] > chith[rr] > chith[cc] :
                bhar =bhar+ 1
print(bhar)
