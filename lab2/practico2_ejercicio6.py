# formula de iteracion Xn+1 = 2^(Xn-1) para resolver la ecuacion 2X - 2^X = 0
# ie f(X) = 2X - 2^X sea g(x) = 2^(X-1) = 2^X / 2 => f(X) = 2X - 2 * g(X)   ahora sea si existe un punto fijo P en g
# 
# => se cumpliria que f(P) = 2P - 2 * g(P) = 2P - 2 * P (pues P es punto fijo de g) por lo tanto f(P) = 0
# 
# #
from practico2_ejercicio5 import *

funcion_ptF = lambda x : 2**(x-1) 

hx = ripf(funcion_ptF,0 , 1e-5, 100)

print(f"Por lo tanto la raiz de f sera {hx[-1]}")