def DoiCoSo(Coso,str):
    number_10=int(str,2)
    res=""
    while number_10!=0 :
        du=number_10%Coso
        number_10//=Coso
        if du>=10:
             res=chr(du-10 + ord('A')) + res
        else:
             res=chr(du + ord('0')) + res
    return res
for _ in range(int(input())):
    Coso=int(input())
    Str=input()
    print(DoiCoSo(Coso,Str))