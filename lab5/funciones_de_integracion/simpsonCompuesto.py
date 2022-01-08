import numpy as np

def simpson(fun,a,b,N):
	if N%2 != 0:
		print("N debe ser par")
		return None
	h = (b-a)/N
	x = np.linspace(a,b,N+1)
	f = np.array([fun(xi) for xi in x])
	fn = f[-1]

	#hace listas de listas de dos elementos
	f = np.reshape(f[:-1],(-1,2))
	
	f0 = f[0,0]
	#saco el 1
	f_pares = f[1:,0]
	
	f_impares = f[:,1]
	I = (h/3)*(f0 + 2*np.sum(f_pares) + 4*np.sum(f_impares) + fn )
	return I