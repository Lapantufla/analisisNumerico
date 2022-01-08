import matplotlib.pyplot as plt
from math import asin, cos ,pi
import numpy as np

x = np.linspace(0, 1, 50)
y = list(map(asin, x))



polinomio = np.polyfit(x, y, 5)
# Evaluamos en x este ajuste para graficar
eval_y_desviado = np.polyval(polinomio, x)

#plt.plot(x, y, label="recta original")
plt.plot(x, y, '*',label="puntos")
plt.plot(x, eval_y_desviado, label="nueva aproximacion")
plt.legend()
# Una grilla para tener como referencia
plt.grid()
plt.show()
