# Para la codificacion se uso vs code por lo tanto tambien para correrlo se uso vs code
# 
# 
# #

import numpy as np
from ejercicio1_final import rfalsi
from funcion_auxiliar import rbisec

#defino la funcion la cual quiero saber su raiz
funcion = lambda x : x**3 -10 *(x**2)+ 10*x + 1

I = [7, 11]

hx_rfalsi,hf_rfalsi = rfalsi(funcion, I, 1e-5, 100)
num_iter_rfalsi = len(hx_rfalsi)
hx_rbisec, hf_rbisec = rbisec(funcion, I, 1e-5, 100)
num_iter_rbisec = len(hx_rbisec)


print(f"El cero encontrado con el metodo rfalsi es : {hx_rfalsi[-1]} con un error de : {np.abs(hf_rfalsi[-1])}")
print(f"La cantidad de iteraciones con el metodo rfalsi es : {num_iter_rfalsi}")
print(f"El cero encontrado con el metodo rbisec es : {hx_rbisec[-1]} con un error de : {hf_rbisec[-1]}")
print(f"La cantidad de iteraciones con el metodo rbisec es : {num_iter_rbisec}")

if num_iter_rbisec < num_iter_rfalsi:
    print(f"El metodo que hace la menor cantidad de iteraciones es el de Biseccion on un total de : {num_iter_rbisec}")
else:
    print(f"El metodo que hace la menor cantidad de iteraciones es el de Falso-Biseccion con un total de : {num_iter_rfalsi}")