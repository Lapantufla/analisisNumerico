import numpy as np
from math import e
import matplotlib.pyplot as plt

# y = a * e ** (b*x)
# ln(y) = ln(a) + ln(e ** (b*x))
# ln(y) = ln(a) + (b*x)
#
# y_p = ln(y)
# x_p = x       y_p = B + b*x_p
#B = ln(a)
# A = b

data = np.loadtxt('./covid_italia.dat', delimiter=",", dtype=np.string_)

number_days_of_th_first_contagion = len(list(data))
#parseo la lista a enteros
number_of_contagion = list(map(int,data[:,1]))
intervalo = np.linspace(1, number_days_of_th_first_contagion, number_days_of_th_first_contagion)

y_p = np.log(number_of_contagion)

coefs = np.polyfit(intervalo, y_p, 1)

A = coefs[0]
a = np.exp(coefs[1])

print(f'Coef. A = {A}, Coef C = {a}.')

plt.plot(intervalo, number_of_contagion, '*')
plt.plot(intervalo, a * (e ** (intervalo * A)))
plt.show()