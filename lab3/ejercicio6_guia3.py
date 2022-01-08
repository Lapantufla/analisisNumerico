import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from ejercicio2_guia3 import inewton
from ejercicio1_guia3 import ilagrange

data = [(-3,1),(-2,2),(-1,5),(0,10),(1,5),(2,2),(3,1)]
#practicando con el map
x_inter = list(map(lambda x : x[0],data))
y_inter = list(map(lambda x : x[1],data))

print(x_inter)

#para el intervalo
a = -1
b = 1
h = (b-a)/199
intervalo = [-1 + h*i for i in range(200)]

#interpolacion usando interp1d
polinomio_interp1d = interp1d(x_inter, y_inter, kind='cubic' , fill_value='extrapolate' )
test = polinomio_interp1d(intervalo)
plt.plot(intervalo,test, label="polinomio interp1d")
#interpolacion usando inewton
polinomio_newton = inewton(x_inter, y_inter, intervalo)
plt.plot(intervalo,polinomio_newton, label="polinomio newton")

#interpolacion usando ilagrange
polinomio_lagrange = ilagrange(x_inter, y_inter, intervalo)
plt.plot(intervalo,polinomio_lagrange, label="polinomio lagrange")

plt.grid()
plt.legend()
plt.show()