def Roat(s):
    k,kq= 0,""
    for i in s:
        k += ord(i)-65
    for i in s:
        kq += chr((ord(i)-65+k)%26+65)
    return kq

def DRM(s):
    s1,s2 = s[:int(len(s)/2)],s[int(len(s)/2):]
    s1,s2 = Roat(s1),Roat(s2)
    kq= ""
    for i in range(len(s1)):
        kq += chr((ord(s1[i])+ord(s2[i])-65*2)%26+65)
    return kq
t = int(input())
for i in range(t):
    s = input()
    print(DRM(s))