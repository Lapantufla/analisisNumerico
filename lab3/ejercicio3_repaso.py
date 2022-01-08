from ejercicio2_guia3 import inewton
from math import cos, pi
import matplotlib.pyplot as plt
import numpy as np

fun_1_sobre_x  = lambda x : 1/x 

x_i = [1, 2, 3, 4, 5]
f_i = [fun_1_sobre_x(x) for x in x_i]
# otra forma de hacer linspace : z_iReal = [24/25 + j/25 for j in range(1,102)]
z_i = np.linspace(1, 5, 101)
f_z_i = [fun_1_sobre_x(x) for x in z_i]

funcionInterp_newton = inewton(x_i, f_i, z_i)

plt.plot(z_i, f_z_i, label="Funcion 1/x")
plt.plot(z_i, funcionInterp_newton, label="Interpolacion via Newton")
plt.grid()
plt.legend()
plt.show()
