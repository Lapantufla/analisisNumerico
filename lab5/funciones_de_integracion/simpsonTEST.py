import numpy as np

def simpson(fun,a,b,N):
    h = (b - a) / N
    n = N // 2
    firts_sum = 0
    secnd_sum = 0
    
    for j in range(1, n): 
        firts_sum += fun(a + (2*j * h))
    firts_sum = 2 * firts_sum

    for j in range(1, n + 1):
        secnd_sum += fun(a + ((2*j - 1) * h))
    secnd_sum = 4 * secnd_sum

    res_corchete = fun(a) + firts_sum + secnd_sum + fun(b)
    S = h/3 * res_corchete

    return S