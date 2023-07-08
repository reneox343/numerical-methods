#--- Función f(x,y) de la fórmula de Euler
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
f = lambda x,y: (x+y-1)**2
#---- Paso de integración
dx_list = [0.05]
#---- Condiciones iniciales
x0 = 1
y0 = 2
#---- x máximo a resolver
xmax = 1.25
#----------------------
DataEulerList = []
DataHeunList = []

for k1 in range(len(dx_list)):
    dx = dx_list[k1]
    #----------------------
    points = int((xmax-x0)/dx)+1
    #----------------------
    x = x0
    yEuler = y0
    yHeun = y0
    #----------------------
    DataEuler = np.array([[x,yEuler]])
    DataHeun = np.array([[x,yHeun]])
    for k in range(points):
        #Metodo de Euler
        yEuler = yEuler + dx*f(x,yEuler)
        #Metodo de Heun
        pNext = yHeun + dx*f(x,yHeun)
        yHeun = yHeun + 0.5*dx*(f(x,yHeun) + f(x+dx,pNext))

        x = x + dx
        #--------------------------
        DataEuler = np.concatenate((DataEuler,np.array([[x,yEuler]])))
        DataHeun = np.concatenate((DataHeun,np.array([[x,yHeun]])))
    #------------------------------------------
    DataEulerList.append(DataEuler)
    DataHeunList.append(DataHeun)

#----------- Graficación Euler
n_cases = len(DataEulerList)
for k in range(n_cases):
    DataEuler = DataEulerList[k]
    print("Euler")
    print(DataEuler)
    x = DataEuler[:,0]
    yEuler = DataEuler[:,1]
    plt.plot(x,yEuler,label= "dx = " + str(x[1]-x[0]) + " (Euler)")

#----------- Graficación Euler
n_cases = len(DataHeunList)
for k in range(n_cases):
    DataHeun = DataHeunList[k]
    print("Heun")
    print(DataHeun)
    x = DataHeun[:,0]
    yHeun = DataHeun[:,1]
    plt.plot(x,yHeun,label= "dx = " + str(x[1]-x[0])+ " (Heun)")
#----------- SolucionExacta
# fExact = lambda x:np.exp(x)
# xExact = np.linspace(x0,xmax,100)
# yExact = fExact(xExact)
# plt.plot(xExact,yExact,label= "Exacta")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()