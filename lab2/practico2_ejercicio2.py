from practico2_ejercicio1 import rbisec
import matplotlib.pyplot as plt
import numpy as np
import math 

#inciso a)

fun_tg = lambda x : (2*x) - math.tan(x)
hx,hf = rbisec(fun_tg, [0.8, 1.4], 1e-5, 100)

print("Inciso A)")
print(f"Los valoes de hx: {hx} \n y  hf: {hf}")

#inciso b)

#fun_x_quad = lambda x : x**2 - 3
#hx,hf = rbisec(fun_tg, [0.8, 1.4], 1e-5, 100)

print("Inciso B)")
print(f"Los valoes de hx: {hx} \n y  hf: {hf}")

#inciso c)
def grafico_inciso_A(hx, hf):
    intervalo = np.linspace(-1, 1.5, 100)
    f_val = [fun_tg(x) for x in intervalo]

    plt.plot(hx, hf, "*", label="Sucesion de Biseccion(Raiz)")
    plt.plot(intervalo, f_val, label="Funcion f(x) = 2X- tan(X)")
    plt.legend()
    plt.grid()
    plt.show()


grafico_inciso_A(hx, hf)