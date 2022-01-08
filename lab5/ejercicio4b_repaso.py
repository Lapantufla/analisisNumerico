import numpy as np
import matplotlib.pyplot as plt
import math
from funciones_de_integracion.simpsonTEST import simpson

fun_ej_b = lambda x : x * math.sin(x)
I_exacta = math.sin(1) - math.cos(1)
print(f"Valor exacto integral: {I_exacta}") 

#cota de error:
#encontramos la cuarta derivada cuarta de f  = x * sen(x)- 4* cos(x)
#en el intervalo [0,1] la funcion tiene un maximo en 1 y <= -1 por lo tanto puedo acotar por -1

i = 2
y = []
cota_error_S = 1
while cota_error_S > 1e-5: 
    cota_error_S =  1/180 * ((1/i)**4) 
    y.append(simpson(fun_ej_b, 0, 1, i))
    i += 2
print(f"Valor aproximado por metodo de Simpson : {y[-1]}")
error_abs = abs(y[-1] - I_exacta)
print(f"El error absoluto al aproximar la integral por el metodo del Simpson es: {error_abs}")
