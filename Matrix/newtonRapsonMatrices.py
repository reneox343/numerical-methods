import numpy as np
import sympy as sp
class newtonRapsonMatrices:
    def __init__(self) -> None:
        #valores
        self.x0 = np.matrix([[-0.2],[-0.2],[0.1]])
        #simbolos
        x = sp.Symbol("x")
        y = sp.Symbol("y")
        z = sp.Symbol("z")
        self.simbolos = [x,y,z]
        #ecuaciones
        f1 = (x**2)*y+sp.cos(3*x)-z
        f2 = x-y**2+z**2
        f3 = x+y-z
        self.ecuaciones = [f1,f2,f3]
        self.jacobiano = self.crearJacobiano()
        #tolerancia
        self.tolerancia = 1e-3

    def crearJacobiano(self):
        jacobiano = []
        for ecuacion in self.ecuaciones:
            linea = []
            for sym in self.simbolos:
                linea.append(ecuacion.diff(sym))
            jacobiano.append(linea)
        return jacobiano

    def evaluarJacobianoInv(self,xk):
        J = []
        for linea in self.jacobiano:
            L = []
            for columna in linea:
                L.append(float(columna.evalf( subs={self.simbolos[0]:xk[0,0], self.simbolos[1]:xk[1,0] ,self.simbolos[2]:xk[2,0] })))
            J.append(L)
        J = np.matrix(J)
        J = np.linalg.inv(J)
        return J

    def evaluarFunciones(self,xk):
        E = list()
        for ecuacion in self.ecuaciones:
            E.append([float(ecuacion.evalf(subs={self.simbolos[0]:xk[0,0], self.simbolos[1]:xk[1,0] ,self.simbolos[2]:xk[2,0]}))])
        E = np.matrix(E)
        return E

    def calcular(self):
        xk = self.x0
        self.evaluarFunciones(xk)
        k = 0
        print()


        while True:
            print("iteracion(K): ",k)
            k+=1
            print()
            anterior = xk
            print(f"x{k-1}:\n",anterior)
            xk = xk - self.evaluarJacobianoInv(xk)*self.evaluarFunciones(xk)
            norma = np.linalg.norm(xk-anterior)
            print(f"x{k}:\n",xk)
            print(f"norma(x{k}-x{k-1}):",norma)
            print()
            if(norma <= self.tolerancia):
                break


#empezar
new = newtonRapsonMatrices()
new.calcular()
