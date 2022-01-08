import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import math

#ejercicio a
func_ej_a = lambda x : math.exp(-x**2)

res_a= quad(func_ej_a, np.inf, -np.inf)
print(f"El resultado de la integracion del inciso a es: {res_a[0]} y el error: {res_a[1]}")

#ejercicio b
func_ej_b = lambda x : x**2 * np.log(x + np.sqrt(x**2 + 1))

res_b = quad(func_ej_b, 0, 2)
print(f"El resultado de la integracion del inciso b es: {res_b[0]} y el error : {res_b[1]}")