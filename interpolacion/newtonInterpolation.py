import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
class NewtonInterpolation:
    def calculate(self,x,y,p = 1):
        matrix = list()
        for i in range(0,len(x)):
            row = list([0]*len(x))
            for j in range(0,len(y)):
                if(j == 0):
                    row[j] = y[i]
            matrix.append(row)
        cont = 1
        for i in range(1,len(x)):
            for j in range(1,len(y)):
                if(j>i):
                    continue
                matrix[i][j] = (matrix[i][j-1] - matrix[i-1][j-1])/(x[i] - x[i-j])
            cont+=1
        print("matriz:")
        print(np.matrix(matrix))

        xs = sp.Symbol("x")
        pList = list()
        
        for i in range(0,p):
            if(i == 0):
                # p1x = matrix[0][0] + matrix[1][1]*(xs-x[0])
                pk = matrix[i][i] + matrix[i+1][i+1]*(xs-x[i])
                pList.append(pk)
            else:
                string = f"{matrix[i+1][i+1]}*"
                for j in range(0,i+1):
                    string+=f"(x-{x[j]})*"
                string = string.replace("--","+")
                string = string.replace("+-","-")
                string = string.replace("-+","-")
                string = string[0:len(string)-1]
                pk = pList[i-1] + sp.parse_expr(string)
                pk = sp.expand(pk)
                pList.append(pk)
        print()
        print("polinomio: ",str(pList[p-1]).replace("**","^"))
        print()
        print("comprobacion:")
        for i in range(0,len(x)):
            print(f"x: {x[i]}, y=f(x): {y[i]}={float(pList[p-1].evalf( subs={xs:x[i]}))}")
        self.graficar(x,y,xs,pList[p-1])
        return pList[p-1]

    def graficar(self,x,y,xs,func):
        fig,ax1 = plt.subplots(1,1)
        for i in range(0,len(x)):
            ax1.scatter( x= x[i],y = y[i],color = 'red')

        x = np.linspace(x[0],x[len(x)-1],100)
        row = list()
        for xk in x:
            row.append(float(func.evalf( subs={xs:xk})))
        # print(row)
        len(x)
        # y = np.linspace(x,stop=len(row)+1)
        len(row)
        ax1.plot(x,row, 'black')
        ax1.plot([x[0],x[len(x)-1]],[0,0], color = 'black',linestyle='dashed')
        plt.show()
  
newton1 = NewtonInterpolation()
newton2 = NewtonInterpolation()
#1:4
f1 =newton1.calculate([0,0.41888,0.83776,1.2566],[1,1.8135,2.4863,2.9021],3)
#4:
f2 =newton2.calculate([1.2566,1.6755,2.0944,2.5133],[2.9021,2.989,2.7321,2.1756],3)

func = f1 + f2
x = sp.Symbol("x")
print(f"0.1: {float(func.evalf( subs={x:0.1}))}")
print(f"0.5: {float(func.evalf( subs={x:0.5}))}")
print(f"1.4: {float(func.evalf( subs={x:1.4}))}")
print(f"2.4: {float(func.evalf( subs={x:2.4}))}")
