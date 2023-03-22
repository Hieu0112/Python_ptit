# import queue
# def check(n):
#     if "2" in n and "3" in n and "5" in n and "7" in n:
#         return  True
#     return False
# n=int(input())
# q=queue.Queue()
# for i in "2357":
#     q.put(i)
# while q.empty() == False:
#     res=q.get()
#     if len(res) < n:
#         for i in "2357":
#             q.put(res+i)
#     if len(res) < 4 or res[-1] == '2':
#         continue
#     if check(res) :
#         print(res)
def resolve(res, a, b, c, d, length):
    if a + b + c + d == length:
        if res[-1] != '2' and a != 0 and b != 0 and c != 0 and d != 0 :
            print(res)
    else :
        resolve(res + '2', a + 1, b, c, d, length)
        resolve(res + '3', a, b + 1, c, d, length)
        resolve(res + '5', a, b, c + 1, d, length)
        resolve(res + '7', a, b, c, d + 1, length)
for i in range(4 ,int(input()) + 1):
    resolve("", 0, 0, 0, 0, i)