import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# 50x + 24y <= 2400
# 30x + 33y <= 2100
# despejo y
# y_1 <= 100-50/24*x
# y_2 <= 2100/33 - 30/33*x
#  #

x = np.linspace(0,50, 100)

#condiciones:
cond_1 = 100 - 50/24 * x 
con_2 = 2100/33 - 30/33 * x 
#para que quede bonito
max_restriccion = np.minimum(cond_1, con_2)
max_restriccion_positive = np.maximum(max_restriccion, 0)
plt.fill_between(x, max_restriccion)
plt.show()
