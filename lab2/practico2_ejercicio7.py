
import math
import matplotlib.pyplot as plt
from practico2_ejercicio1 import rbisec
from practico2_ejercicio3 import rnewton
from practico2_ejercicio5 import ripf

def usando_Bisec(x):
    	# calcula u(x) = y
	fun_auxiliar = lambda y : y - math.exp(-(1-x*y)**2)
	hy, hu = rbisec(fun_auxiliar, [0.0,2.0], 1e-6, 100)
	y = hy[-1]
	return y

def usando_Newton(x):
	# calcula u(x) = y
	fun_auxiliar = lambda y : (y - math.exp(-(1-x*y)**2), \
		1 - math.exp(-(1-x*y)**2)*(-2*(1-x*y)*(-x)))
	hy, hu = rnewton(fun_auxiliar, 1.0, 1e-6, 100)
	y = hy[-1]
	return y

def usando_ptoFijo(x):
	fun_auxiliar = lambda y : math.exp(-(1-x*y)**2)
	hy = ripf(fun_auxiliar, 1.0, 1e-6, 100)
	y = hy[-1]
	return y

#x = np.linspace(0.0, 1.5, 100)
h = 1.5/99
x = [i*h for i in range(100)]
y_bisec = [usando_Bisec(xi) for xi in x]
y_newton = [usando_Newton(xi) for xi in x]
y_ipf = [usando_ptoFijo(xi) for xi in x]

fig,ax = plt.subplots(3,1)

ax[0].plot(x,y_bisec, label="beseccion")
ax[1].plot(x,y_newton, label="newton")
ax[2].plot(x,y_ipf, label="punto_fijo")
plt.show()

plt.plot(x,y_ipf,'g')
plt.plot(x,y_bisec,'--r')
plt.plot(x,y_newton,'ob')
plt.show()
