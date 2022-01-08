
import numpy as np
import matplotlib.pyplot as plt
import math
from funciones_de_integracion.trapeciocompuesto import trapecio

fun_ej_a = lambda x : x * math.exp(-x)

#cota de error:
#encontramos la segunda derivada de f ie f''(x) =(x-2)e^(-x)
#en el intervalo 0 1 obtiene un maximo en x=1 con y <= -0.3 por lo tanto puedo acotar la funcion por 0.3
i = 1
cota_error_T = 1
y = []
I_exacta = math.exp(-1)*(math.e - 2)
print(f"Valor exacto integral: {I_exacta}") 

#para simpson es lo mismo nada mas que cambia la variable cota_error
while cota_error_T > 1e-5: 
    cota_error_T =  1/12 * ((1/i)**2) * 0.3 
    y.append(trapecio(fun_ej_a, 0, 1, i))
    i += 1
print(f"Valor aproximado por metodo de trapecio : {y[-1]}")
error_abs = abs(y[-1] - I_exacta)
print(f"El error absoluto al aproximar la integral por el metodo del trapecio es: {error_abs}")

