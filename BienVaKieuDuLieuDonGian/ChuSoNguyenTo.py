def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
for _ in range(int(input())):
    so = input()
    kq = "YES"
    if nt(len(so))==1:
        a = set(so)
        sont,soknt=0,0
        for x in a:
            if nt(int(x)): 
                sont += so.count(x)
            else: 
                soknt += so.count(x)
        if sont>soknt: 
            kq="YES"
        else: 
            kq="NO"
    else: 
        kq="NO"
    print(kq)