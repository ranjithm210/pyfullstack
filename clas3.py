class hero:
    def __init__(self):
        self.name="punithrajkumar"
        self.age="47"
        self.height="5.8"
        self.address="sd"
    def dance(self):
        print("hero is dacing")
    def act(self):
        print("hero is dancing")

h1=hero()

print(h1.name)
print(h1.age)
print(h1.address)
print(h1.height)

h1.height=5.999
h1.address="sadashivanagar"
h1.noofhits=25
h1.noofflops=5
h2=h1
h3=h2
print(h2.name)
print(h1.age)
print(h3.height)
print(h3.address)

h3.dance()
h3.act()