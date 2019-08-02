zz=int(input())
h=list(map(int,input().split()))
xx=[1]*zz
for l in range(zz):
    if (l==0):
        if (h[l]>h[l+1]):
            xx[l]=xx[l]+xx[l+1]
    elif (l>0):
        if( h[l] > h[l-1]):
            xx[l]=xx[l]+xx[l-1]
print(sum(xx))
