# 2 medicamentos, |hierba A| hierba B |dosisparacurar|
#        medicina1|3       |2         |25            |
#        medicina1|4       |1         |20            | 
#        total:   |25      |10        | 
# para curar una persona necesito 25 unidades de med1 o 20 unidades de med2 
#
# sea x_i = 'cantida de medicina i' para i = 1,2  
#
# funcion a max 25 * x_1 + 20 * x_2
#  sujeto a     3*x_1 + 4*x_2 <= 25
#               2*x_1 + x_2 <= 10
# 
# mis funciones seran:
# 1) x_2 <= 25/4 - 3/4x
# 2) x_2 <= 10 - 2x
#
#       
# A_ub= |3   4 |
#       |2   1 |   
# 
# b_ub= |25  10|  
# 
# c =   |25  20|
# #
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


c = - np.array([25.,20])
A_ub = np.array([
                [3,4],
                [2,1]
                ])
b_ub =[25,10]

solucion = optimize.linprog(c, A_ub, b_ub)
print(f"SOLUCION : {solucion}")

x = np.linspace(0,5,100)


cond_1 = 25/4 - 3/4 * x
cond_2 = 10 - 2 * x 

min_restriccion = np.minimum(cond_1, cond_2)
positive_restriccion = np.maximum(min_restriccion, 0)

plt.plot(solucion.x[0], solucion.x[1], "*", color="red")
plt.fill_between(x, positive_restriccion)
plt.legend()
plt.grid()
plt.show()