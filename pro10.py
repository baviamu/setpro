bhat=int(input())
chott=[int(u) for u in input().split(" ")]
cheti=0
for t in range(bhat):
      for y in range(t):
           if(chott[y]<chott[t]):
                cheti+=chott[y]
print(cheti)
