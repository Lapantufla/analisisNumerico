# 
# y(x) = c * x^A 
# ln(y(x)) = ln(c) + A * ln(x)
# =>
#   y_ = ln(y(x)) 
#   c_ = ln(c) =>
#   x_ = ln(x) 
# 
# => y_ = c_ + A * x_
# #

import numpy as np
import math 
import matplotlib.pyplot as plt

data = np.loadtxt("./datos/datos3a.dat")
x_i = data[0]
x_i_sombrero = np.log(x_i)
y_i = data[1]
y_i_sombrero = np.log(y_i)

coefs = np.polyfit(x_i_sombrero, y_i_sombrero, 1)

A = coefs[0]
C_ = coefs[1]
c = np.exp(C_)

aprox_points = np.polyval(coefs, x_i)
plt.plot(x_i, c * (x_i ** A) , label="funcion aproximada")
plt.plot(x_i, y_i, "*", label="puntos a aproximar")

plt.legend()
plt.grid()
plt.show()
























