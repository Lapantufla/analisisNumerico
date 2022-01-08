import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#costos es una matris 100 * 100
datos_costos = np.loadtxt("./Datos/costos.dat")
datos_stock = np.loadtxt("./Datos/stock.dat")
datos_demanda = np.loadtxt("./Datos/demanda.dat")

c = datos_costos.flatten()

b_ub = np.hstack([datos_stock, datos_demanda])

#stock

#s




