bav=input()
for bha in range(len(bav)):
  if(bav[bha] < bav[bha+1]):
    print(bav[bha+1:])
    break
