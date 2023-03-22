s=input()
dem={'hoa':0,'thuong':0}
for i in s:
    if i.islower() :
        dem['thuong']+=1
    else :dem['hoa']+=1
print(s.upper() if(dem['hoa']>dem['thuong']) else s.lower())