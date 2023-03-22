class Rectangle:
    def __init__(self,height,width,mau):
        self.height = height
        self.width = width
        self.mau = mau
    def perimeter(self):
        return 2*(self.width+self.height)
    def area(self):
        return self.width*self.height
    def color(self):
        return self.mau.title()

arr = input().split()
if int(arr[0])<=0 or int(arr[1])<=0:
    print('INVALID')
else:         
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))