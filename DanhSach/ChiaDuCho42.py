a = []
s = set()
while True:
    a = a + [int(x) for x in input().split()]
    if len(a) == 10 : break
for i in a:
    s.add(i % 42)
print(len(s))
