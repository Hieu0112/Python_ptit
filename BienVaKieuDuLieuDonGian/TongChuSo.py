t = input()
dem=0
while len(t)>1:
    tongcs=0
    dem +=1
    if t[0] == "-": tongcs +=ord('-')-ord('0')
    else : tongcs +=int(t[0])
    for i in t[1:]:
        tongcs += int(i)
    t = str(tongcs)
print(dem)
