import numpy as np
import matplotlib.pyplot as plt

class Graper:

    def __init__(self):
        self.fig, (self.ax1) =plt.subplots(1,1)
        self.fig.canvas.manager.set_window_title('grapher')

    def f(self,x:float):
        return (1/(255**2)+(x*600-(1/x*500)))**(1/2)

    def createGraph(self,a,b,line):
        distance = abs(a-b)
        #draw fucntion
        x = np.linspace(-distance,distance,100000)
        x = 1/x
        y = self.f(x)
        self.ax1.plot(x,y, 'black')
        #draw y=0 line
        # self.ax1.plot([-distance,distance],[line,line], color = 'black',linestyle='dashed')
        #draw original range
        self.ax1.plot([a,a],[y.min(),y.max()], color = 'red',linestyle='dashed')
        self.ax1.plot([b,b],[y.min(),y.max()], color = 'red',linestyle='dashed')
        plt.show()
# 91528546.656017
grapher = Graper()
# x=91528546.656017-100000000*np.pi
# print(x)
# print(grapher.f(x))
grapher.createGraph(1,100,1500000)