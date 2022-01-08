import numpy as np
import math
import matplotlib.pyplot as plt
from lagrange_aux import *
from funciones_auxiliares import *

def ivander(x, y, z):
    cantidad_filas = len(x)
    cantidad_columnas = cantidad_filas
    #inicializo la matriz n*n
    A = np.zeros((cantidad_filas, cantidad_columnas))
    
    #construyo la matriz A correspondiente a mis puntos x_i
    for i in range(0, cantidad_filas):
        for j in range(0, cantidad_columnas):
            A[i][j] = x[i]**j    
    

    #uso sullu ya que me di cuenta que es mas preciso que soleg
    coefs_u = sollu( A, y)

    #invierto los coefs
    coefs_flip = np.flip(coefs_u)

    result_evals_in_z = np.polyval(coefs_flip, z)

    return result_evals_in_z
    

func_sen  = lambda x : math.sin(x)

vector_x = np.linspace(0, 2 * math.pi, 55)
vector_y = [func_sen(x) for x in vector_x]
vector_z = np.linspace(0, 2 * math.pi, 100)

result_lagrange = ilagrange(vector_x, vector_y, vector_z)
result_ivander = ivander(vector_x, vector_y, vector_z)

plt.plot(vector_x, vector_y, "x", label="puntos a interpolar")
plt.plot(vector_z, result_lagrange, label="funcion lagrange")
plt.plot(vector_z, result_ivander, label="funcion ivander" )

plt.legend()
plt.show()


