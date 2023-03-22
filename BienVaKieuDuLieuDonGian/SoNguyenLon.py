def UCLN(a,b):
    while a*b!=0:
        if a>b:a%=b
        else:b%=a
    return a+b
for _ in range(int(input())):
    print(UCLN(int(input()),int(input())))