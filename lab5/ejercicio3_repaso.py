import numpy as np
import matplotlib.pyplot as plt
import math
from funciones_de_integracion.trapeciocompuesto import trapecio

fun_senit = lambda x : math.cos(x)
fun_sen = lambda x : math.sin(x)

def senit(x):
    y = []
    for x_i in x: 
        ctdad_intervalos = math.ceil(x_i / 0.1)
        if ctdad_intervalos != 0:    
            y.append(trapecio(fun_senit, 0, x_i, ctdad_intervalos))
        else :
            y.append(0)
    return y
    
#notar que quiero puntos que disten de 0.5, por lo tanto la cantidad de puntos que tendre sera 2pi / 0.5 = 12.5 ie 13
ctidad_puntos = math.ceil(math.pi * 2 / 0.5)
intervalo = np.linspace(0, 2 * math.pi, ctidad_puntos )



y_i_senit = senit(intervalo)
y_i_sen = [fun_sen(x) for x in intervalo]

print("tamaño",y_i_senit)

plt.plot(intervalo, y_i_senit, label="funcion senit")
plt.plot(intervalo, y_i_sen, "*",label="funcion seno")
plt.legend()
plt.grid()
plt.show()


