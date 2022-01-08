import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from funciones_de_integracion.simpsonTEST import simpson



def pendulo(longitud, alpha):
    alpha = np.deg2rad(alpha)
    periodo = lambda theta : 1/np.sqrt(1 - (np.sin(alpha / 2)**2) * np.sin(theta)**2)

    res_integracion = simpson(periodo, 0, np.pi / 2, 1024)

    print(f"El resultado de la integracion es: {res_integracion} ")

    T = 4 * np.sqrt(longitud/ 9.8) * res_integracion
    return(T)


result = pendulo(1, 45)

print(f"El resultado del ejercicio es:{result}")