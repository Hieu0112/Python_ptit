modulo = 1000

def pow(a, b):
    if b == 0:
        return pair(1, 0)
    if b & 1:
        return mul(pow(a, b-1), a)
    p = pow(a, b >> 1)
    return mul(p, p)
def mul(a, b):
    r = pair(0, 0)
    r.x = (a.x*b.x + 5*a.y*b.y) % modulo
    r.y = (a.x*b.y + a.y*b.x) % modulo
    return r
class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) :
        return f'{self.x} {self.y}'
x = pair(3, 1)
for case in range(int(input())):
    print(f'Case #{case+1}: '+str(pow(x, int(input())).x*2 % modulo - 1).zfill(3))