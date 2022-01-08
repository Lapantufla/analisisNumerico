import numpy as np
from scipy.linalg import lu

def soltrsup(A,b):
    #si no es invertible, cortar
    try:
        #no es muy optimo verificar singularidad invirtiendo la matriz
        np.linalg.inv(A)
    except Exception as e:
        print("El sistema no tiene solución")
        return e

    n = A.shape[0]
    x = b.copy()

    for i in range(n - 1, -1 , -1):
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x

def soltrinf(A,b):
    #si no es invertible, cortar
    try:
        np.linalg.inv(A)
    except Exception as e:
        print("El sistema no tiene solución")
        return e

    n = A.shape[0]
    x = b.copy()

    #Si es invertible, tiene solución
    for i in range(n):
        for j in range(i):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x

def sollu(A,b):
    P,L,U = lu(A)
    y = soltrinf(L,P.T @ b)
    x = soltrsup(U,y)
    return x