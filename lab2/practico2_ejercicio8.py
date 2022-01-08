# calcular el minimo de f en [0, pi/2], donde 
# f(x) = tan(x)/x**2 => f'(x) = - [2tan(x) - x*sec^2(x)]/x^3
# notar que sec(x) = 1/cos(x) => sec(x)^2 = 1/cos(x)^2
#
# por lo tanto me fijare en el x  tq f'(x) = 0 ie 0 = -2tan(x) - x* sec(x)^2
# 
# 
# 
# #
from practico2_ejercicio3 import rnewton
import numpy as np
import math 

funcion_del_minimo = lambda x : math.tan(x)/x**2

def fun(x):
    f = - 2 * math.tan(x) + x*(1/(math.cos(x)**2))
    df = 3 * 1/(math.cos(x)**2) + 2 * x * 1/(math.cos(x)**2) * math.tan(x)
    return (f,df)

#considerando el intervalo [0, pi/2]
hx,hf= rnewton(fun, 0.5, 1e-6, 100)

print(f"El x en donde la derivada es igual a 0 se da en x = {hx[-1]}")
candidato_minimo = hx[-1]

valor_minimo_de_funcion = funcion_del_minimo(candidato_minimo)

print(f"El valor minimo de la funcion es: {valor_minimo_de_funcion}")