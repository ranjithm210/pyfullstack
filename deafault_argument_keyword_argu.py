class demo:
    def demo(self,x=11,y=22,z=33):
        print(x)
        print(y)
        print(z)

d1=demo()
a=10
b=20
c=30
d1.demo (b,c)
d1.demo (a,)
d1.demo (a,b,)
d1.demo (a,b,c)
