import numpy as np

def puntomedio(fun, a, b, N):

    h = (b - a ) / ( N + 2)
    n = (N // 2) + 1

    sum = 0
    for j in range(0, n):
        sum += fun((a + (2 * j + 1)* h))
    
    return (2*h*sum)
   

    
