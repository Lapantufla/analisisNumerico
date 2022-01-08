import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# 
#        [52, 212, 25, 60]
# A_ub = [57, 218, 23, 57]
#        [51, 201, 26, 54]
#        [56, 223, 21, 55]
# 
# b_ub = [220, 300, 245, 190]
# 
# c = [68.3, 69.5, 71, 71.2]
# 
# #

c = - np.array([68.3, 69.5, 71, 71.2])
A_ub = np.array([
                [52, 212, 25, 60],
                [57, 218, 23, 57],
                [51, 201, 26, 54],
                [56, 223, 21, 55]
])
b_ub = [220, 300, 245, 190]

solucion = optimize.linprog(c, A_ub, b_ub)

print(f"Esta es la solucion:{solucion}")


