import sys,string


def maxOfSegmentMins(ja, ma, sa):
    if sa == 1:
        return min(ja)
    if sa == 2 :
        return max(ja[0], ja[ma - 1])
    return max(ja)

ma,sa = input().split()
ma,sa = int(ma),int(sa)
ja = [ int(x) for x in input().split()]
ma = len(ja)
ans = maxOfSegmentMins(ja, ma, sa)
print(ans)
