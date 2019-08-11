bavu="Dhoni"
nivu=input()
amu=list(set(bavu)-set(nivu))
chith26=list(set(nivu)-set(bavu))
amu=len(amu)+len(chith26)
if amu==0:
	print("yes")
else:
	print("no")
