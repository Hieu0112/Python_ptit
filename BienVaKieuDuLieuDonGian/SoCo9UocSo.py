a=[0]*100000
a[0]=1
a[1]=1
for i in range(2,100000):
	if a[i]==0:
		for j in range(i*2,100000,i):
			a[j]=1
s=int(input())
dem=0
for i in range(2,int(s**0.5)+1):
    if a[i]==0:
        if i**8<=s:
            dem+=1
        for j in range(i+1,int(s**0.5)+1):
            if a[j]==0:
                if i**2*j**2<=s:
                    dem+=1
                else :
                    break
print(dem)