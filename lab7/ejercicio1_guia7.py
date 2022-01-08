import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
## x = cuanto tengo que comprar de T1 y T2
## (x1 := cantidad de T1, x2 := cantidad de T2)
## c = valores de cada kilo de fertilizante (10, 8)
## 3 restricciones  NPK

## x1 * 3 + x2 * 2 >= 3 (P)
## x1 * 1 + x2 * 3 >= 1.5 (N)
## x1 * 8 + x2 * 2 >= 4 (K)

## quedaria en :

## x1 * -3 + x2 * -2 <= -3 (P)
## -x1 * 1 - x2 * 3 <= -1.5 (N)
## -x1 * 8 - x2 * 2 <= -4 (K)
##       [-3, -2]
## A_ub= [-1, -3]
#        [-8, -2] 
#
# b_ub = [-3, -1.5, -4]


c = np.array([10.,8])
A_ub = np.array([
                [-3, -2],
                [-1, -3],
                [-8, -2]
                ]
                )
b_ub =np.array([-3, -1.5, -4])

solucion = optimize.linprog(c, A_ub, b_ub)

print(f"Este es el resultado {solucion}")

x = np.linspace(0, 2)
#corresponde a las condiciones
cond_p = -1.5 * x + 1.5
cond_n = -1/3 * x + 0.5
cond_k = -4 * x + 2
#y1 = -3/2 * x + 3/2
#Esto es una cota, para que quede lindo nomas
y2 = 4

max_restriccion = np.maximum(cond_p, cond_n)
max_restriccion = np.maximum(max_restriccion, cond_k)
plt.plot(solucion.x[0], solucion.x[1], "*", color="red")
plt.fill_between(x, max_restriccion, y2)

plt.show()