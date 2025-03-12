 

class student:
    def __init__(self):
        self.name="ramu"
        self.age="22"
        self.mobl_no="456789"
        self.address="banglore"
        self.qualification="B_E"

    def eat(self):
        print("student is eating")
    def walking(self):
        print("student is walking")
    def study(self):
        print("student is studying") 

f1 = student()

print(f1.name)
print(f1.age)
print(f1.mobl_no)
print(f1.address)
print(f1.qualification)
f1.eat()
f1.walking()
f1.study()
