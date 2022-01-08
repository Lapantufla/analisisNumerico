from scipy.integrate import quad
import numpy as np
import math
from funciones_auxiliares import *

# sistema = Kx = w, donde w = [g*m1, g*m2, g*m3] tenemos que m1 = 2kg; m2 = 3kg; m3 = 2.5kg y k = 10kg/s^2
# 
# tenemos el sig sistema:
#                         °2k*(x2 - x1) + m1*g - k*x1 = 0
#                         °k*(x3 - x2) + m2*g - 2k*(x2 - x1) = 0
#                         °m3*g - k*(x3-x2) = 0
# 
# despejando m_i obtenemos el sig sistema:
#                           
#                         °(-2*k)/g * x2 + (3*k)/g * x1            = m1
#                         °-k/g * x3 + (3*k)/g * x2 - (2*k)/g * x1 = m2
#                         °k/g * x3 - k/g * x2                     = m3                          
#
#  


def calcular_inversa(A):
    ctidad_filas = len(A)
    e1 = [1, 0, 0]
    e2 = [0, 1, 0]
    e3 = [0, 0, 1]

    inversa_c1 = sollu(A, e1)
    inversa_c2 = sollu(A, e2)
    inversa_c3 = sollu(A, e3)

    #creo una matriz donde las filas son las columnas de la matriz inversa
    columnas_dinversa = np.array([inversa_c1,inversa_c2, inversa_c3] )

    matriz_inversa = np.zeros((ctidad_filas,ctidad_filas))
    for i in range (0,ctidad_filas):
        for j in range (0, ctidad_filas):
            #inicializo por columnas, construyo la inversa inicializando las columnas primero
            matriz_inversa[j][i] = columnas_dinversa[i][j]

    #supongo que debe haber una forma mucho mas sencilla de inicializar una matriz por las culumnas y no las filas pero no encontre :c

    return matriz_inversa



def sistema_masas_suspendidas():
   
    k = 10
    g = 9.8
    b = [2, 3, 2.5]
    
    A = np.zeros((3, 3))
    A = [
        [3*k/g, -2*k/g, 0 ],
        [-2*k/g, 3*k/g, -k/g],
        [ 0,     -k/g,   k/g]
        ]

    resultado_a = sollu(A,b)
    print(f"El valor de la solucion del item a) es: {resultado_a}")
 
    inversa_dA = calcular_inversa(A)

    print(f"El valor de la solucion del item b) es: \n{inversa_dA}")
    
def ejercicio_practico():
    A = np.zeros((3,3))
    A = [
        [18,8,6],
        [8,6,2],
        [6,2,4]
        ]
    b = [-2.78, -1.59, -1.62]
    resultado_a = sollu(A,b)
    print(f"El valor de la solucion del items a) es: {resultado_a}")

ejercicio_practico()

b = [35.2501, 55.7502]