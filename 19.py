hu=int(input())
fi=[]
t=[]
for q in range(hu):
    fi.append(list(map(int,input().split())))
for list1 in fi:
    for num in list1:
        t.append(num)
t.sort()
for q in t:
    print(q,end=' ')
