import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# 2 medicamentos especiales
# SOLO DISPONEMOS DE 25 UNIDADES DE A Y 10 UNIDADES DE B
#  Para la medicina 1 :
#           3 unidades de hierba A
#           2 unidades de hierba  B
# con 25 unidades puede curar una persona
# Para la medicina 2:
#           4 unidades de hierba A
#           1 unidad de hierba B
# con 20 unidades puede curar una persona
# 
# X1 = cantidad de medicina1; X2 = cantidad medicina2 
# c = medicinas necesarias para curar 1 people(25 20)
# x1 * 3 + x2 * 4 <= 25
# x1 * 2 + x2 * 1 <= 10
# 
#         [3, 4]         
#  A_ub = [2, 1]
#   
# b_ub = [25, 10] 
# 
c = - np.array([25., 20])
A_ub = np.array([
                [3, 4],
                [2, 1]
                ])
b_ub = [25, 10]

solucion = optimize.linprog(c, A_ub, b_ub)

print(f"El resultado optimo es {solucion}")

#ojo aca
x = np.linspace (0,4, 100)
cond_1 = - 3/4 * x + 25/4
cond_2 = 10 - 2 * x

max_retriccion = np.minimum(cond_1, cond_2)
plt.plot(solucion.x[0], solucion.x[1], "*", color="red")
plt.fill_between(x, max_retriccion, 2)
plt.legend()
plt.grid()
plt.show()
