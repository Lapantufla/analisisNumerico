
def ripf(fun, X0, err, mit):
    hx = []
    X_aux = X0
    hx.append(X_aux)

    for i in range(mit):
        X_aux = fun(X_aux)
        hx.append(X_aux)

        if abs(hx[i] - hx[i+1]) < err:
            break
    
    return hx