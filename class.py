 

class fan:
    def __init__(self):
        self.brand="bajaj"
        self.colour="white"
        self.cost="1500"
        self.no_of_blades="3"

    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("fan is off") 
        self.speed="5000rpm"
f1 = fan()

print(f1.brand)
print(f1.colour)
print(f1.cost)
print(f1.no_of_blades)
f1.on()
f1.rotate()
f1.off()
print(f1.speed)
f1.run=20
print(f1.run)