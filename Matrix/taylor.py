import numpy as np
import sympy as sp
class Taylor:
    def __init__(self) -> None:
        #cambiar los valosres aqui
        self.x0 = 0.5
        self.k = 4
        x = sp.Symbol("x")
        self.x = x
        self.fx = 2 * sp.cos(2*x)+ sp.sin(x)
    def calcular(self):
        self.funciones = []
        self.evaluadas = []
        self.errores = []
        derivada = self.fx
        for i in range(0,self.k): 
            if(i == 0):
                self.funciones.append(1)
                self.evaluadas.append(1)
                r = self.fx.evalf( subs={self.x:1}) - 1
                self.errores.append(r)
                continue
            derivada = derivada.diff(self.x)
            p = (derivada.evalf(subs={self.x:self.x0})/np.math.factorial(i))*((self.x-self.x0)**i)
            p = p + self.funciones[i-1]
            val = p.evalf( subs={self.x:1})
            r = self.fx.evalf( subs={self.x:1}) - val
            self.errores.append(r)
            self.funciones.append(p)
            self.evaluadas.append(val)
    def imprimirResultados(self):
        print()
        print('{:<10s} {:<10s} {:<10s}'.format('k','pk(1)','error'))
        for i in range(0,self.k): 
            print('{:<10d} {:<10.12f} {:<10.12f}'.format(i,self.evaluadas[i],self.errores[i]))
    def impimirFunciones(self):
        print()
        print("funciones")
        for func in self.funciones:
            print(str(sp.expand(func)).replace("**","^"))
            
t = Taylor()
t.calcular()
t.imprimirResultados()
t.impimirFunciones()