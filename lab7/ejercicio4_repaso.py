# sea R,N,B las variables "cantidad de cerveza Rubia..negra..respectivamente"
# => voy a querer maximizar c = 7R + 4N + 3B
#         sujeto a R+2N+2B <= 30
#                  2R+ N+ 2B <= 45 
# 
# => A_ub = |1  2  2|
#           |2  1  2|
# 
#  b= |30   45|
#    
# c = (7, 4, 3)
# 
#  #


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


c = - np.array([7, 4, 3])

A_ub = np.array([
                [1, 2, 2],
                [2, 1, 2]
])

b_ub = np.array([30, 45])

solucion = optimize.linprog(c, A_ub, b_ub)
print(f"El resultado optimo es {solucion}")