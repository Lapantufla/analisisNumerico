import matplotlib.pyplot as plt

from funciones_de_integracion.trapeciocompuesto import trapecio
from funciones_de_integracion.simpsonCompuesto import simpson

import numpy as np

def intenumcomp(fun, a, b, N, regla):
    if(regla == 'Trapecio'):
        S = trapecio(fun, a, b, N)
    elif (regla == 'Simpson'):
        S = simpson(fun, a, b, N)
    
    return S

fun = lambda x : np.exp(-x)

I_exacta = - np.exp(-1) + np.exp(0)



print(f"Resultado intervalo = {N}")    
I = intenumcomp(fun,0,1,N,'Trapecio')
err_exacto = np.abs(I-I_exacta)
cota_error = (1/180) * (1/N)**4
print(f"El valor aproximado es I={I}")
print(f"El error exacto de integrar con N={N} intervalos es e={err_exacto} y la cota es c={cota_error}")