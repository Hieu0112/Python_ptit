# x=set()
# n = int(input())
# def kt(a,b,c,r,str):
#     # if 1<=a<=b<=c : x.add(str)
#     print(str)
#     if r<=0: return
#     if a<=n//3: kt(a+1,b,c,r-1,str+"A")
#     if b<=(n-1)//2: kt(a,b+1,c,r-1,str+"B")
#     if r>=1: kt(a,b,c+1,r-1,str+"C")
# kt(0,0,0,n,"")
# # x = sorted(x,key = lambda i : (len(i),i))
# # for i in x:
# #     print(i)

# n=int(input())
# x=set()
# def Sinh(str,a,b,c):
#     if a!=0 and a<=b and b<=c:
#         x.add(str)
#     if a + b + c == n :
#         return
#     Sinh(str + 'A' ,a + 1, b ,c)
#     Sinh(str + 'B' ,a ,b + 1,c)
#     Sinh(str + 'C' ,a, b, c + 1)
# Sinh("",0,0,0)
# x = sorted(x,key = lambda i : (len(i),i))
# for i in x:
#     print(i)

def resolve(str,a,b,c,length):
    if a!=0 and a<=b and b<=c and length==len(str):
        print(str)
    if len(str) < length :
        resolve(str + 'A' ,a + 1, b ,c ,length)
        resolve(str + 'B' ,a ,b + 1,c ,length)
        resolve(str + 'C' ,a, b, c + 1 ,length)
for i in range(3, int(input()) + 1) : 
    resolve("", 0, 0, 0, i)