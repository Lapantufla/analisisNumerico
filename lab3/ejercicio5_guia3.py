import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

data = np.loadtxt('./datos_aeroCBA.dat')

years = data[:,0]
temp = data[:,1]

#asi saco los nan que no los quiero para interpolar
not_nan = ~np.isnan(temp)

temp_interp = temp[not_nan]
years_interp = years[not_nan]

print("ES DE TIPO", type(temp_interp))

polinomio = interp1d(years_interp, temp_interp, kind = 'cubic', fill_value='extrapolate' )

anios_plot = np.arange(1957,2018)
temps_plot = polinomio(anios_plot)

plt.plot(anios_plot, temps_plot)
plt.plot(years_interp, temp_interp,'o')
plt.grid()
plt.show()

