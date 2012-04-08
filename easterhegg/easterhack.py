import sys
(s,c,m,w,k,z,b)=("Easterhegg",0,int(sys.argv[1]),sys.stdout.write,0,lambda p:s[p%len(s)],[])
for v in [g for g in list(bin(0x471000)[2:].zfill(30)) for _ in range(m*2)]:
	if not k%(5*m*2):b+=["\n"];w(''.join(b*m));b=[]
	if int(v):b+=[" "]
	else:b+=[z(c)];c+=1
	k+=1
