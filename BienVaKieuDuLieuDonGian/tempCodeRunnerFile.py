import queue
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