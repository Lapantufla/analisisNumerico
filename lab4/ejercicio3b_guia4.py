import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('./datos/datos3b.dat')

# y = x /( A * x + B)
# 1/y = (A * x + B) * 1/x
# x/y = A * x + B


x = datos[0]
y = datos[1]

coefs = np.polyfit(x, x/y, 1)

A = coefs[0]
B = coefs [1]

intervalo = np.linspace(np.min(x), np.max(x), 100)

plt.plot(x, y, '*')
plt.plot(intervalo, intervalo/(A * intervalo + B))
plt.legend()
plt.show()

