import matplotlib.pyplot as plt

from funciones_de_integracion.trapeciocompuesto import trapecio
from funciones_de_integracion.puntomedioCompuesto import puntomedio
from funciones_de_integracion.simpsonCompuesto import simpson
from funciones_de_integracion.simpsonTEST import simpson as simpsonTEST

import numpy as np



def intenumcomp(fun, a, b, N, regla):
    if(regla =='Punto-medio'):
        S = puntomedio(fun, a, b, N)
    elif(regla == 'Trapecio'):
        S = trapecio(fun, a, b, N)
    elif (regla == 'Simpson'):
        S = simpsonTEST(fun, a, b, N)
    
    return S


fun = lambda x : np.exp(-x)

# valor exacto de la integral:
I_exacta = - np.exp(-1) + np.exp(0)

print(f"El valor exacto de la integral es I={I_exacta}")

intervalos = [4,10,20]

for N in intervalos:
    #simpson
    print(f"Resultado intervalo = {N}")    
    I = intenumcomp(fun,0,1,N,'Simpson')
    err_exacto = np.abs(I-I_exacta)
    cota_error = (1/180) * (1/N)**4
    print(f"El valor aproximado es I={I}")
    print(f"El error exacto de integrar con N={N} intervalos es e={err_exacto} y la cota es c={cota_error}")

    
    #puntomedio
    """ 
    print(f"Resultado intervalo = {N}")    
    I = intenumcomp(fun,0,1,N,'Punto-medio')
    err_exacto = np.abs(I-I_exacta)
    cota_error = (1/6) * (1/(N + 2))**2
    print(f"El valor aproximado es I={I} con punto medio")
    print(f"El error exacto de integrar con N={N} intervalos es e={err_exacto} y la cota es c={cota_error}")
    """
    """
    #trapecio
    print(f"Resultado intervalo = {N}")    
    I = intenumcomp(fun,0,1,N,'Trapecio')
    err_exacto = np.abs(I-I_exacta)
    cota_error = (1/12) * (1/N)**2
    print(f"El valor aproximado es I={I} con trapecio")
    print(f"El error exacto de integrar con N={N} intervalos es e={err_exacto} y la cota es c={cota_error}")""" 

#trapecio

fun2 = lambda x : np.exp(-x**2)
solucion = intenumcomp(fun2,0,1,355,'Trapecio')

print("ESTE ES EL RESULTADO", solucion)