import numpy as np
import sympy as sp
def func(x,y):
    xf = 0
    yf = 0
    x2 = 0
    x3 = 0
    x4 = 0
    xy = 0
    x2y= 0
    for i in range(len(x)):
        xf += x[i]
        yf += y[i]
        x2 += x[i]**2
        x3 += x[i]**3
        x4 += x[i]**4
        xy += x[i]*y[i]
        x2y += (x[i]**2)*y[i]

    matriz = np.asmatrix([[len(x),xf,x2],[xf,x2,x3],[x2,x3,x4]])
    print("matriz")
    print(matriz)
    ak = np.asmatrix([[yf],[xy],[x2y]])
    print("ak")
    print(ak)
    matrizINV = np.linalg.inv(matriz)
    print("matrizINV")
    print(matrizINV)
    resultado = matrizINV*ak
    print("resultado")
    print(resultado)
x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
y = [6.3098,8.8223,9.8419,10.966,9.4835,9.3035,6.2408,2.6802,-2.6173,-7.0794,-14.141]
func(x,y)
xs = sp.Symbol("x")
f = sp.parse_expr(f"-2.00776737*(x**2)+5.98333319*x+6.22874965")
for data in x:
    print(f"f({data}) = ",f.evalf(subs={xs:data}))
