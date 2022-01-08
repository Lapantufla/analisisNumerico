import math as mt
import numpy as np

fun_tg = lambda x : (2*x) - mt.tan(x)

def rbisec (fun, I, err, mit):
    #asumo que el intervalo de entrada esta ordenado
    a = I[0]
    b = I[1]
    
    hx = []
    hf = []

    if fun(a) * fun(b) >= 0:
        #tienen igual signo so el teorema no puede ejecutarse
        return None

    if a >= b:
        #en un intervalo ordenado a no deberia ser mayor a b
        return None

    for it in range(mit):
        c = (a + b) / 2
        fun_evaluado_c  = fun(c)

        #append es para enlistar
        hx.append(c)
        hf.append(fun_evaluado_c)

        if abs(fun_evaluado_c) < err:
            print("Llegamos a un cero :)")
            break

        if fun_evaluado_c * fun(a) < 0:
            b = c

        else:    
            a = c
            
    return (hx, hf)

#hx,hf = rbisec(fun_tg, [0.8, 1.4], 1e-5, 100)

#print(f"Los valoes de hx: {hx} y hf: {hf}")
