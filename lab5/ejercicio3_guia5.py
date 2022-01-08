import matplotlib.pyplot as plt
import math

from funciones_de_integracion.trapeciocompuesto import trapecio
from funciones_de_integracion.puntomedioCompuesto import puntomedio
from funciones_de_integracion.simpsonCompuesto import simpson

import numpy as np

def func_sen(x):
    return math.cos(x)

def func_a_comparar(x):
    return math.sin(x)

def senint(x):
    #aca lo que hago es hacer sub-intervalos te tamaño 0.1
    ctdad_intervalos = math.ceil(x / 0.1)
    if ctdad_intervalos != 0 :
        result = trapecio(func_sen, 0, x, ctdad_intervalos)
    else:
        result = 0
    return result


#veo cuantos intervalos de 0.5 puedo hacer
ctdad_intervalos = math.ceil(2 * math.pi / 0.5)

print(f"cuantos es ctidad de intervalos {ctdad_intervalos}")
#hago los intervalos desde 0 hasta 2*pi espaciados con 0.5
intervalo = np.linspace(0, 2 * math.pi, ctdad_intervalos)

f_val = [func_a_comparar(x) for x in intervalo]

senint_val = []
for i in intervalo :
    result = [senint(i)]
    senint_val += result
    

plt.plot(intervalo, f_val, label="funcion_seno")
plt.plot(intervalo, senint_val, "*", label="funcion_senit")
plt.grid()
plt.legend()
plt.show()