#cota para trapecio es -(b-a)/12import matplotlib.pyplot as plt

from funciones_de_integracion.trapeciocompuesto import trapecio

from funciones_de_integracion.simpsonCompuesto import simpson

import math
import numpy as np

#f = -(x + 1) * e ** -x

I_exacta = - 2/math.e +1


fun = lambda x : x * np.exp(-x)

fun_derivada = lambda x :  -(1 - x) * np.exp(- x) - np.exp( -x)

I = trapecio(fun, 0, 1, 30)
if( I_exacta - I < 10e-5 ):
    print("PRINTEO ESTO Bicho",I)
print("PRINTEO ESTO ",I_exacta - I)


# 1/12 * 1/n**2 *2 < 10e-5
#                1/n**2  < 10e-5 / 2 * 12
#                       n > raiz 1/(10e-5 / 2 * 12)  
#cota_del_error = N  > 1/raiz(10e-5 *12* (-1/0.3))


    