Set={}
dem=0
ss=""
for _ in range(int(input())):
    s=input()
    if len(s)==0:
        dem=0
    else : 
        if dem==0:
            Set[s]=0
            ss=s
        else:
            Set[ss]+=1
        dem=1
for i in Set:
    print(str(i)+": "+str(Set[i]))

