# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:09:43 2022

@author: uidr0032
"""

import numpy as np
def get_Xnext(Xk):
    xk = Xk[0]
    yk = Xk[1]
    zk = Xk[2]
    wk = Xk[3]
    ##jacobi
    xnext = (-25+2*yk-3*zk-2*wk)/8
    ynext = (23-zk-3*wk)/9
    znext = (-41-2*yk-wk)/7
    wnext = (31-5*yk-zk)/7
    ##Gauss-Seidel 
    # xnext = (-25+2*yk-3*zk-2*wk)/8
    # ynext = (23-zk-3*wk)/9
    # znext = (-41-2*ynext-wk)/7
    # wnext = (31-5*ynext-znext)/7
    return np.array([xnext,ynext,znext,wnext])


Xk = np.array([2,-2,5,8])
max_iter = 40
tol = 1e-3
print("***segunda tarea ejercicio 1 Gauss-Seidel***")
print('{:<10s} {:<10s} {:<10s} {:<10s} {:<10s} {:<10s}'.format('k','x','y','z','w','norma'))
print('-----------------------------------------------------------')
print('{:<10d} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10s}'.format(0,Xk[0],Xk[1],Xk[2],Xk[3],'--'))

for k in range(max_iter):
    Xnext = get_Xnext(Xk)
    norma = np.linalg.norm(Xnext-Xk)
    print('{:<10d} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}'.format(k+1,Xnext[0],Xnext[1],Xnext[2],Xnext[3],norma))
    if norma<=tol:
        break
    else:
        Xk = Xnext
    
