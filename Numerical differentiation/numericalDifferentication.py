import numpy as np
class ForwardDiferences:
    #change formula
    def f(self,x):
        return np.cos(x)

    def firtOrder(self,x0,h):
        return (-3*self.f(x0)+4*self.f(x0+h)-self.f(x0+h*2))/(2*h)
    
    def secondOrder(self,x0,h):
        return (2*self.f(x0)-5*self.f(x0+h)+4*self.f(x0+h*2) - self.f(x0+h*3))/(h**2)

    def thirdOrder(self,x0,h):
        return (-5*self.f(x0)+18*self.f(x0+h)-24*self.f(x0+h*2)+14*self.f(x0+h*3)-3*self.f(x0+h*4))/((h**3)*2)

class BackwardDiferences:
    #change formula
    def f(self,x):
        return np.cos(x)

    def firtOrder(self,x0,h):
        return (3*self.f(x0)-4*self.f(x0-h)+self.f(x0-h*2))/(2*h)
    
    def secondOrder(self,x0,h):
        return (2*self.f(x0)-5*self.f(x0-h)+4*self.f(x0-h*2) - self.f(x0-h*3))/(h**2)

    def thirdOrder(self,x0,h):
        return (5*self.f(x0)-18*self.f(x0-h)+24*self.f(x0-h*2)-14*self.f(x0-h*3)+3*self.f(x0-h*4))/((h**3)*2)

class CentralDifferences:
    #change formula
    def f(self,x):
        return np.cos(x)
    
    def firtOrder(self,x0,h):
        return(self.f(x0+h)-self.f(x0-h))/(2*h)

    def secondOrder(self,x0,h):
        return(self.f(x0+h)-2*self.f(x0)+self.f(x0-h))/(h**2)
    
    def thirdOrder(self,x0,h):
        return (self.f(x0+2*h)-2*self.f(x0+h)+2*self.f(x0-h)-self.f(x0-2*h))/(2*(h**3))
forward = ForwardDiferences()
backward = BackwardDiferences()
central = CentralDifferences()

print("forward")
print(forward.firtOrder(0.8,0.001))
print(forward.secondOrder(0.8,0.001))
print(forward.thirdOrder(0.8,0.001))
print("back")
print(backward.firtOrder(0.8,0.001))
print(backward.secondOrder(0.8,0.001))
print(backward.thirdOrder(0.8,0.001))
print("central")
print(central.firtOrder(0.8,0.001))
print(central.secondOrder(0.8,0.001))
print(central.thirdOrder(0.8,0.001))