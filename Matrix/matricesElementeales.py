from __future__ import division
from base64 import b16encode
import numpy as np
from numpy.lib.function_base import copy
class MatraicesElementales:
    def __init__(self,matriz) -> None:
        self.filas = len(matriz)
        self.columnas = len(matriz[0])
        self.matriz = matriz
        self.P = self.calculaP(matriz)
        self.matrix = np.matrix(matriz,float) 
        self.U =  self.P*np.matrix(matriz,float)
        self.L = None
        self.identidad = np.identity(self.filas)

    def crearIdentidad(self,matriz):
        identidad = copy(matriz)
        for i in range(0,self.filas):
            for j in range(0,self.columnas):
                if(i == j ):
                    identidad[i][j] = 1
                else:
                    identidad[i][j] = 0
        return identidad
        
    def calculaP(self,matriz):
        P=[]
        #inicializar
        for i in range(0,self.filas):
            fila = []
            for j in range(0,self.filas):
                fila.append(0)
            P.append(fila)
        #crear identidad
        solucionado = True
        filasSolucionadas = []
        for i in range(0,self.columnas):
            solucionado = False
            for j in range(0,self.filas):
                if( solucionado or j in filasSolucionadas or matriz[j][i] == 0):
                    continue
                P[j][i] = 1
                filasSolucionadas.append(j)
                solucionado = True
        return np.matrix(P,float)

    def calcular(self):
        elemetales = list()
        #U
        for i in range(0,self.columnas):
            for j in range(0,self.filas):
                if(i == j):
                    continue
                if(j<i):
                    continue
                item=self.U.item(i,i)
                elemetal = copy(self.identidad)
                elemetal.itemset(j,i,float(-self.U.item(j,i))/float(item))
                elemetales.append(elemetal)
                self.U =  elemetal*self.U 
        #L
        self.L = np.linalg.inv(elemetales[0]) 
        for i in range(1,len(elemetales)):
            self.L = self.L + np.linalg.inv(elemetales[i])
        for i in range(0,self.filas):
            self.L.itemset(i,i,1)
    #b es una matriz transpuesta
    def LYb(self,b,p):
        self.yk = list()
        for i in range(0,self.filas):
            sumas = 0
            for j in range(0,self.columnas):
                value = self.L.item(i,j)
                if(value ==1):
                    break
                sumas += value * self.yk[j]
            sumas = -sumas + b[i]
            self.yk.append(sumas)
        if(p):
            print()
            for i in range(0,len(self.yk)):
                print(f"y{i+1}: {self.yk[i]}")
        return self.yk

    def UXy(self,y,p):
        self.xk = list()
        for i in range(self.filas,0,-1):
            i-=1
            sumas = 0
            divition = 1
            for j in range(self.columnas,0,-1):
                j-=1
                if(i==j):
                    divition = self.U.item(i,j)
                    break
                value = self.U.item(i,j) 
                sumas += value * self.xk[(j-self.columnas+1)*-1]
            sumas = (-sumas + y[i])/divition
            self.xk.append(sumas)
        self.xk.reverse()
        if(p):
            print()
            for i in range(0,len(self.xk)):
                print(f"x{i}: {self.xk[i]}")
        self.xk.reverse()
        return self.yk
                
    def comprobacion(self,b):
        print()
        print("comprobacion")
        for i in range(0,self.filas):
            adicion = 0
            for j in range(0,self.columnas):
                adicion += self.matriz[i][j] * self.xk[j]
            print(f"{adicion} = {b[i]}")

            


        

##cuadrada, caso 2
# LU =MatraicesElementales([[2,3,2,4],[4,10,-4,0],[-3,-2,-5,-2],[-2,4,4,-7]])
##0 
# LU = MatraicesElementales([[0,2,3],[2,-4,7],[1,-2,-5]])
##mas filas que columnas , caso 4
# LU = MatraicesElementales([[3,-1,4,2],[1,2,-3,5],[2,4,1,5]])
## mas columnas que filas ,caso 5
# LU = MatraicesElementales([[1,2,3,],[-1,-4,5],[6,-3,2],[4,1,-12]])
#caso 7
# LU = MatraicesElementales([[2,3,2,4],[4,10,-4,0],[-3,-2,-5,-2],[-2,4,4,-7]])
#tarea  caso 1
# LU = MatraicesElementales([[1,5,0,7],[1,9,0,3],[3,-2,8,2],[7,2,0,1]])
#tarea caso 2
LU = MatraicesElementales([[8,-2,3,2],[0,5,1,7],[0,9,1,3],[0,2,7,1]])

LU.calcular()
print("matriz:\n",LU.matrix)
print("P:\n",LU.P)
print("U:\n",LU.U)
print("L:\n",LU.L)
print("L*U:\n",LU.L*LU.U)
print("matriz * P:\n",LU.P *LU.matrix)
b =[-25,31,23,-41]
y = LU.LYb(b,True)
# y = LU.LYb([4,-8,-4,-1],True)
x = LU.UXy(y,True)
# LU.comprobacion(b)