class student:
    def __init__(self,name,usn,mbl,address):
        self.name=name
        self.usn=usn
        self.mbl=mbl
        self.address=address

s1=student("rama","1vtu001","1111","bnglore")
s2=student("sita","rty56","123456","dfgh")
print(s1.name)
print(s2.name)