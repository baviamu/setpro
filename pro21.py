cvv1=int(input())
cvv2=list(map(int,input().split()))
th=int(cvv1/2)
x=cvv2[:th]
y=cvv2[th::]
if ((sum(x)//len(x))==(sum(y)//len(y))):
    print("yes")
else:
    print("no")
