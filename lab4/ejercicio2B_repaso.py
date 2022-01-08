import numpy as np
from math import asin, cos ,pi
import matplotlib.pyplot as plt


funcion_a = lambda x : cos(x)

x_i = np.linspace(0, 4 * pi, 50)
y_i = list(map(funcion_a, x_i))

coefs_vector = np.polyfit(x_i, y_i, 5)
interpolate_points = np.polyval(coefs_vector, x_i)

plt.plot(x_i, interpolate_points, label="Funcion Aproximacion de los puntos")
plt.plot(x_i, y_i, "*" ,label="puntos a aproximar")
plt.legend()
plt.grid()
plt.show()

print("ARRAY", x_i)