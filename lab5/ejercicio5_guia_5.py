from scipy import integrate
import numpy as np

fun = lambda x : np.exp(-x**2)

result = integrate.quad(fun, -np.inf, np.inf)

print(result)