#   
# E = 0.01328 D^2*V^3
# 
# E = energia generada
#
# D = diametro en metros 
# 
# V = velocidad del viento
# 
# ----
# 500W = 0.01329 * D^2 * (24)^3
# 
# raiz[500W /(24^3 * 0.01329)] = D
# 
# #
from practico2_ejercicio3 import rnewton
import numpy as np
import math 

def fun(x):
    # g = 0.01328*X**2 * Y **3
    # 0 = (0.01328)*X**2 * (24)**3 - 500
    # 0 = 183.58272*X**2 - 500 = f(x) => f'(x) = 367.16544 * X
    f = 183.58272 * (x**2) - 500
    df = 367.16544 * x
    return (f,df)

hx,hf = rnewton(fun, 20, 1e-5, 100)

print(f"El Diametro del molino deberia ser de : {hx[-1]} metros")

