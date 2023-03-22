import queue
for _ in range(int(input())):
    qe = queue.Queue()
    lst='012'
    qe.put('1')
    qe.put('2')
    s = []
    n=int(input())
    while n> 0:
        a = qe.get()
        if a.count("2") > a.count("0") + a.count("1"):
            s.append(a)
            n -=1
        for c in lst:
            qe.put(a + c)
    print(" ".join(s))
