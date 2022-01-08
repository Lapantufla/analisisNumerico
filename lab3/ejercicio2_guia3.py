def divided_differences(x, y):
    n_coef= len(x)
    coefs = y.copy()
    
    for idx in range(n_coef - 1):
        for jdx in reversed(range(idx + 1, n_coef)):
            coefs[jdx] = (coefs[jdx] - coefs[jdx - 1])/ (x[jdx] - x[jdx - idx - 1])

    return coefs

def inewton(x, y, z):
    w = []
    k = len(x)
    c_i = divided_differences(x, y)
    for z_i in z:
        w_i = 0.0
        for idx in range(k): # idx = 1 hasta 4, k = 5
            prod = 1.0
            for jdx in range(idx): # hasta 1
                prod = prod * (z_i - x[jdx])
            
            w_i = w_i + c_i[idx] * prod    
          
        w.append(w_i)
    
  
    return w




