from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import iterable, select
from decimal import Decimal


class FalsePosition:

    def __init__(self,tolerance:int,precisionTable:int,distance):
        self.fig, (self.ax1,self.ax2) =plt.subplots(1,2)
        self.fig.canvas.manager.set_window_title('falsePosition')
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

    def __createTable(self,solutionPosition):
        colLabels = ["iteration", "a", "b","c","f(a)","f(b)","f(c)"]
        table =self.ax1.table(cellText=self.iteration,colLabels=colLabels,loc="center")
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table[(solutionPosition[0],solutionPosition[1])].set_facecolor("#56b5fd")
        table[(solutionPosition[0],solutionPosition[1]+3)].set_facecolor("#56b5fd")
        plt.show()

    def __addIteration(self,i,a,b,c,fa,fb,fc):
        fa = self.__formatNumber(fa)
        fb = self.__formatNumber(fb)
        fc = self.__formatNumber(fc)
        self.iteration.append([i,a,b,c,fa,fb,fc])

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


    def calculate(self,a,b):
        self.__createGraph(a,b)
        #
        i = 0
        solution = 0
        while(True):
            a = self.__formatNumber(a)
            b = self.__formatNumber(b)
            fa = self.f(a)
            fb = self.f(b)
            c = b - fb*((b-a)/(fb-fa))
            c = self.__formatNumber(c)
            fc = self.f(c)
            self.__addIteration(i,a,b,c,fa,fb,fc)
            if(self.isZero(fa)):
                solution = a
                solutionPosition = [i+1,1]
                break
            if(self.isZero(fb)):
                solution = b
                solutionPosition = [i+1,2]
                break
            if(self.isZero(fc)):
                solution = c
                solutionPosition = [i+1,3]
                break
            #initiation of next iteration
            if(fa*fc>=0):
                a = c
                b = b
            if(fb*fc>=0):
                a = a
                b = c
            # b = b
            # a = c
            i+=1

        #table
        self.__createGraphIntersection(solution,self.f(solution))
        print("solucion:",solution)
        print("solucion evaluada:",self.f(solution))
        self.__createTable(solutionPosition)






falsePosition = FalsePosition(6,6,10)
falsePosition.calculate(-4,2)