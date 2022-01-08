import numpy as np
import matplotlib.pyplot as plt
import math
from funciones_de_integracion.simpsonTEST import simpson

fun_ej_c = lambda x : (1 + x**2)**(3/2)

I_exacto = (3 * math.asin(1) + 7 * math.sqrt(2))/8
print(f"Valor exacto integral: {I_exacto}") 
#cota de error:
#encontramos la cuarta derivada cuarta de f = 1/(x^2 + 1 )^5/2
#en el intervalo [0,1] la funcion tiene un maximo en 0 donde y <= 1 por lo tanto puedo acotar por 1



i = 2
y = []
cota_error_S = 1
while cota_error_S > 1e-5: 
    cota_error_S =  1/180 * ((1/i)**4) 
    y.append(simpson(fun_ej_c, 0, 1, i))
    i += 2
print(f"Valor aproximado por metodo de Simpson : {y[-1]}")
error_abs = abs(y[-1] - I_exacto)
print(f"El error absoluto al aproximar la integral por el metodo del Simpson es: {error_abs}")
print("Cantidad iteraciones: ", len(y))