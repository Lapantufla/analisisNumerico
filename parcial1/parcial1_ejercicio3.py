import numpy as np
import matplotlib.pyplot as plt 
from parcial1_ejercicio2 import busqueda_ceros
from horn_aux import horn

def polinomio(x):
    #P(x)= x **3 + x - 5
   
    valued_fun = horn([1,0,1,-5], x)
    valued_df = horn([3,0,1], x)
    
    return (valued_fun, valued_df)

#para correr descomentar:
#cero_finded = busqueda_ceros(polinomio, 10.0, -10.0, 1e-6, 15)
#print("El cero devuelto por la funcion es: ", cero_finded)
