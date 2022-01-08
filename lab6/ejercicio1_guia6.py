import numpy as np

def soltrinf(A, b):
        
    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None

    n = A.shape[0]
    x = np.zeros(n)
    
    #donde n son la cantidad de filas o de columnas
    n = len(b)
    for i in range(0, n):
        sum = 0
        for j in range(1, i):
            sum += A[i][j] *x[j] 
        x[i] = (b[i] - sum)/A[i][i]
    
    return x

def soltrup(A, b):
    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None
    
    n = A.shape[0]
    x = np.zeros(n)
    #donde n son la cantidad de filas o de columnas
    n = len(b)
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += A[i][j] *x[j] 
        x[i] = (b[i] - sum)/A[i][i]
