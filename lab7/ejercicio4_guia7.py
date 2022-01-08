import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#   MALTA
#   x1_rubia * 1 + x2_negra * 2 +  x3_bajagrd * 2<= 30
#   
#   LEVADURA
#   x1_rubia * 2 + x2_negra * 1 + x3_bajagrd * 2 <= 45
#
#         [1, 2, 2]
#   A_ub= [2, 1, 2]
# 
#   b_ub = [30, 45] 
# 
# x = cantidad de cerveza rubia
# y = cantidad de cerveza negra
# z = cantidad de cerveza baja
# ganancia = 7 * x + 4 * y + 3 * z
# maximizar cT * w es lo mismo que minimizar (-cT) * w 
c = - np.array([7., 4, 3])
A_ub = np.array([
                [1, 2, 2],
                [2, 1, 2]
])
b_ub =np.array([30, 45])
solucion = optimize.linprog(c, A_ub, b_ub)

print(f"Esta es la solucion:{solucion}")


