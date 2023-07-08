from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import iterable, select
from decimal import Decimal


class FalsePosition:

    def __init__(self,tolerance:int,precisionTable:int,distance):
        self.fig, (self.ax1,self.ax2) =plt.subplots(1,2)
        self.fig.canvas.manager.set_window_title('secant')
        self.tolerance =np.float64( "0."+ "0"*(tolerance-1)+"1")
        self.precision = precisionTable
        self.ax1.axis('tight')
        self.ax1.axis('off')  
        self.iteration = []
        self.distance = distance

    def f(self,x):
        return x**3-(7*(x**2))-(9*x)+63
    
    def isZero(self,num):
        num = abs(num)
        if(num == 0 or num == 0.0):
            return True
        return (num<=self.tolerance)

    def __createTable(self):
        colLabels = ["iteration", "xk", "f(xk)"]
        table =self.ax1.table(cellText=self.iteration,colLabels=colLabels,loc="center")
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table[len(self.iteration),1].set_facecolor("#56b5fd")
        table[len(self.iteration),2].set_facecolor("#56b5fd")
        plt.show()

    def __addIteration(self,i,xk1,fxk1):
        fxk1 = self.__formatNumber(fxk1)
        self.iteration.append([i-1,xk1,fxk1])

    def __formatNumber(self,number):
        return np.round(number,self.precision)

    def __createGraph(self,a,b):
        distance = abs(a-b)+self.distance
        #draw fucntion
        x = np.linspace(-distance,distance,100)
        y = self.f(x)
        self.ax2.plot(x,y, 'black')
        #draw y=0 line
        self.ax2.plot([-distance,distance],[0,0], color = 'black',linestyle='dashed')
        #draw original range
        self.ax2.plot([a,a],[y.min(),y.max()], color = 'red',linestyle='dashed')
        self.ax2.plot([b,b],[y.min(),y.max()], color = 'red',linestyle='dashed')

    
    def __createGraphIntersection(self,x,y):
        self.ax2.plot(x,y, 'o', mew=3, ms=3,color = "red")

                    #x-1,x0
    def calculate(self,xNegativo1,x0):
        self.__createGraph(xNegativo1,x0)
        #agrgar las dos primeras iteraciones
        self.__addIteration(0,self.__formatNumber(xNegativo1),self.f(xNegativo1))
        self.__addIteration(1,self.__formatNumber(x0),self.f(x0))
        i = 1
        solution = 0
        solutionPosition = None
        while(True):
            #xks
            #xk-1
            xk0 = self.__formatNumber(self.iteration[i-1][1])
            xk = self.__formatNumber(self.iteration[i][1])
            #evaluadas
            #f(xk-1)
            fxk0 = self.iteration[i-1][2]
            fxk = self.iteration[i][2]
            #xk+1
            xk1 =  xk - fxk *((xk-xk0)/(fxk-fxk0))
            xk1 = self.__formatNumber(xk1)
            fxk1 = self.f(xk1)
            self.__addIteration(i+1,xk1,fxk1)
            if(self.isZero(fxk1)):
                solution = xk1 
                break
            i+=1
            
            
        #table
        self.__createGraphIntersection(solution,self.f(solution))
        print("solucion:",solution)
        print("solucion evaluada:",self.f(solution))
        self.__createTable()






falsePosition = FalsePosition(6,6,10)
falsePosition.calculate(1,5)