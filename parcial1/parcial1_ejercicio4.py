import numpy as np
import matplotlib.pyplot as plt 

from parcial1_ejercicio2 import busqueda_ceros
from horn_aux import horn
from rnewton_aux import rnewton

def polinomio_2(x):
    return (x**3 + x -5)

def polinomio(x):
    #P(x)= x **3 + x - 5
    valued_fun = horn([1,0,1,-5], x)
    valued_df = horn([3,0,1], x)
    
    return (valued_fun, valued_df)

#me quedo con la data de newton ya que tengo que graficar el metodo que mejor funcione y previamente vi que newton iba mejor
hx_newton, hf_newton = rnewton(polinomio, 10.0, 1e-6, 15)

puntos = [-2]
evals = [polinomio_2(-2)]
for idx in range(-19,40):
    puntos.append(idx * 0.1)
    evals.append(polinomio_2(idx * 0.1))

plt.plot(hx_newton, hf_newton, '*', label="Sucesion de Newton")
plt.plot(puntos, evals, label="funcion")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Funcion F(x) = x^3 + x - 5 y Sucesion de Newton")
plt.legend()
plt.show()