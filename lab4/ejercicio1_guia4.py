import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

data = np.loadtxt("./datos/datos1a.dat")

xi = data[:,0]
yi = data[:,1]
len_data = len(data)

sum_xi = sum(xi)
sum_yi = sum(yi)

sum_xi2 = sum(xi**2)
sum_xi_yi = sum(xi*yi)

# | m       sum_xi  | |a0| = |sum_yi  |
# | sum_xi  sum_xi2 | |a1|   |sum_xiyi|

""" matriz = np.array([[m, sum_xi],[sum_xi, sum_xi2]])
vector = np.array([],[]) """

a0 = (sum_xi2 * sum_yi - sum_xi_yi * sum_xi) / (len_data * sum_xi2 - sum_xi**2)
a1 = (len_data * sum_xi_yi - sum_xi * sum_yi)/(len_data* sum_xi2 - sum_xi**2)

def eval_polinomio (x):
    return a1 * x + a0

plt.plot(xi, yi, '*')

z = np.linspace(0,5,100)
w = eval_polinomio(z)

plt.plot(z, w)
plt.show()