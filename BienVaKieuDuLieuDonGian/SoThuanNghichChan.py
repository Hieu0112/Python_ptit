import queue
for _ in range(int(input())):
    n=int(input())
    x=queue.Queue()
    x.put("2")
    x.put("4")
    x.put("6")
    x.put("8")
    while True:
        so=x.get()
        res=int(so+so[::-1])
        if res>=n:
            break
        print(res,end=" ")
        x.put(so+"0")
        x.put(so+"2")
        x.put(so+"4")
        x.put(so+"6")
        x.put(so+"8")
    print()

