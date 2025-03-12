class farmer:
    r=2.5
    def __init__(self,p,t):
        self.p=p
        self.t=t

    def disp(self):
        si=(self.p*self.t*farmer.r )/100

        print(si)
    
f1=farmer(1000000,45)
f1.disp()
