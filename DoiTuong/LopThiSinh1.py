class SinhVien():
	def __init__(self , name,date,x,y,z):
		self.name=name
		self.date=date
		self.x=x
		self.y=y
		self.z=z
	def __str__(self):
		return self.name+" "+self.date+" "+"%.1f"%(self.x+self.y+self.z)
		# return self.name+" "+self.date+" "+"{:.1f}".format(self.x+self.y+self.z)
s=input()
dt=input()
xx=float(input())
xy=float(input())
xz=float(input())
a= SinhVien(s,dt,xx,xy,xz)
print(a)