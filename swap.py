class demo:
    def swap(self,x,y):#defnaion call
        temp=x
        x=y
        y=temp
        return(x,y)
d1=demo ()

a=10
b=20
print(a)
print(b)
res=d1.swap(a,b)   #method call     
print("after swaping")
print(res)