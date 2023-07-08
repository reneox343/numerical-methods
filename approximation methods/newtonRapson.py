from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import iterable, select
from decimal import Decimal


class newton:

    def __init__(self,tolerance:int,precisionTable:int,distance):
        self.fig, (self.ax1,self.ax2) =plt.subplots(1,2)
        self.fig.canvas.manager.set_window_title('newton')
        self.tolerance = np.float64( "0."+ "0"*(tolerance-1)+"1")
        self.precision = precisionTable
        self.ax1.axis('tight')
        self.ax1.axis('off')  
        self.iteration = []
        self.distance = distance

    def f(self,x):
        return np.tan(x)*65-((9.81*4225)/(1250*(np.cos(x)**2))) + 2
    
    def der_f(self,x):
        return (162500*np.cos(x)-165789*np.sin(x))/2500*np.cos(x)*np.cos(x)*np.cos(x)
    
    def isZero(self,num):
        num = abs(num)
        if(num == 0 or num == 0.0):
            return True
        return (num<=self.tolerance)

    def __createTable(self,solutionPosition):
        colLabels = ["iteration", "xk", "f(xk)","f(xk)'"]
        table =self.ax1.table(cellText=self.iteration,colLabels=colLabels,loc="center")
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table[(solutionPosition[0],solutionPosition[1])].set_facecolor("#56b5fd")
        table[(solutionPosition[0],solutionPosition[1]+1)].set_facecolor("#56b5fd")
        plt.show()

    def __addIteration(self,i,xk,fxk,dfck):
        fxk = self.__formatNumber(fxk)
        dfck = self.__formatNumber(dfck)
        self.iteration.append([i,xk,fxk,dfck])

    def __formatNumber(self,number):
        return np.round(number,self.precision)

    def __createGraph(self,x0):
        distance = abs(x0)+self.distance
        #draw fucntion
        x = np.linspace(-distance,distance,100)
        y = self.f(x)
        self.ax2.plot(x,y, 'black')
        #draw y=0 line
        self.ax2.plot([-distance,distance],[0,0], color = 'black',linestyle='dashed')
    
    def __createGraphIntersection(self,x,y):
        self.ax2.plot(x,y, 'o', mew=3, ms=3,color = "red")


    def calculate(self,x0):
        self.__createGraph(x0)
        i = 0
        solution = 0
        xk = self.__formatNumber(x0)
        self.__addIteration(i,xk,self.f(xk),self.der_f(xk))
        while(True):
            i+=1
            xk = xk -self.f(xk)/self.der_f(xk)
            xk = self.__formatNumber(xk)
            fxk = self.f(xk)
            self.__addIteration(i,xk,fxk,self.der_f(xk))
            if(self.isZero(fxk)):
                solution = xk
                solutionPosition = [i+1,1]
                break
            

        #table
        self.__createGraphIntersection(solution,self.f(solution))
        print("solucion:",solution)
        print("solucion evaluada:",self.f(solution))
        self.__createTable(solutionPosition)

falsePosition = newton(6,6,3)
falsePosition.calculate(10)