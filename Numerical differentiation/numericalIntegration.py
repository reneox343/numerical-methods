import numpy as np
class Helper:

    @staticmethod
    def NodeCreator(a,b,n,h) -> None:
        nodes = list()
        for i in range(0,n):
            nodes.append(a+i*h)
        return nodes
        
    @staticmethod
    def f(x):
        return (1 + (np.e**-x) *np.sin(4*x))

class Trapezodial:

    def calculate(self,a,b,n):
        h = (b-a)/(n-1)
        nodes = Helper.NodeCreator(a,b,n,h)
        result = 0
        for i in range(0,len(nodes)):
            if(i+1 < len(nodes)):
                result += (h/2) * (Helper.f(nodes[i]) + Helper.f(nodes[i+1]))
        print("Trapezodial: ",result)
                
class Simsons:
    def calculate(self,a,b,n):
        h = (b-a)/(n-1)
        nodes = Helper.NodeCreator(a,b,n,h)
        result = 0
        for i in range(0,len(nodes),2):
            try:
                result += h/3*(Helper.f(nodes[i]) + 4*Helper.f(nodes[i+1]) + Helper.f(nodes[i+2]))
            except:
                pass
        print("Simsons: ",result)

class SimsonsThreeEighths:
    def calculate(self,a,b,n):
        h = (b-a)/(n-1)
        nodes = Helper.NodeCreator(a,b,n,h)
        result = 0
        for i in range(0,len(nodes),3):
            try:
                result += (3*h/8)*(Helper.f(nodes[i]) + 3*Helper.f(nodes[i+1]) + 3*Helper.f(nodes[i+2]) + Helper.f(nodes[i+3]))
            except:
                pass
        print("SimsonsThreeEighths: ",result)

class Booles:
    def calculate(self,a,b,n):
        h = (b-a)/(n-1)
        nodes = Helper.NodeCreator(a,b,n,h)
        result = 0
        for i in range(0,len(nodes),4):
            try:
                result += (2*h/45)*(7*Helper.f(nodes[i]) + 32*Helper.f(nodes[i+1]) + 12*Helper.f(nodes[i+2]) + 32*Helper.f(nodes[i+3]) + 7*Helper.f(nodes[i+4]))
            except:
                pass
        print("Booles: ",result)
                

                
trapezodial = Trapezodial()
trapezodial.calculate(0,1,1000000)
simson = Simsons()
simson.calculate(0,1,1000000)
simsonsThreeEighths = SimsonsThreeEighths()
simsonsThreeEighths.calculate(0,1,1000000)
booles = Booles()
booles.calculate(0,1,1000000)