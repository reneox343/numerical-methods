import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#el grado es depende del numero de puntos -1
class Interpolation:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.xs = sp.Symbol("x")
        # f1 = sp.parse_expr("x+1")

    def graficar(self,x,y):
        fig,ax1 = plt.subplots(1,1)
        for i in range(0,len(x)):
            ax1.scatter( x= x[i],y = y[i],color = 'red')
        x = np.linspace(x[0],x[len(x)-1],100)
        row = list()
        for xk in x:
            row.append(self.f(xk))
        # print(row)

        ax1.plot(x,row, 'black')
        ax1.plot([x[0],x[len(x)-1]],[0,0], color = 'black',linestyle='dashed')
        plt.show()

    def f(self,x):
        return float(self.func.evalf(subs={self.xs:x}))

    def calcaulate(self):
        func = ""
        for i in range(0,len(self.y)):
            func += f"{self.y[i]}*"
            numerator = ""
            denominator = ""
            for j in range(0,len(self.x)):
                if(i == j):
                    continue
                numerator += f"(x-{self.x[j]})*"
                denominator += f"({self.x[i]}-{self.x[j]})*"
            func+= "(" +numerator[0:len(numerator)-1] + ")/(" + denominator[0:len(denominator)-1] + ")+"
            func = func.replace("--","+")
            func = func.replace("+-","-")
            func = func.replace("-+","-")
        func = func[0:len(func)-1]
        func = sp.parse_expr(func)
        func = sp.expand(func)
        self.func = func
        print("polinomio: ",str(sp.expand(func)).replace("**","^"))
        print()
        print("comprobacion:")
        for i in range(0,len(self.x)):
            print(f"x: {self.x[i]}, y=f(x): {self.y[i]}={float(func.evalf( subs={self.xs:self.x[i]}))}")
        self.graficar(self.x,self.y)
        
        print(f"0.1: {float(func.evalf( subs={self.xs:0.1}))}")
        print(f"0.5: {float(func.evalf( subs={self.xs:0.5}))}")
        print(f"1.4: {float(func.evalf( subs={self.xs:1.4}))}")
        print(f"2.4: {float(func.evalf( subs={self.xs:2.4}))}")

            
                
            

interpolation = Interpolation([0,0.41888,0.83776,1.2566,1.6755,2.0944,2.5133],[1,1.8135,2.4863,2.9021,2.989,2.7321,2.1756])    


interpolation.calcaulate()