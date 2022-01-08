
def rnewton(fun, x0, err, mit):
    hx = []
    hf = []
    #fun devuelve una funcion y la derivada de la funcion valuada en x0
    f,df = fun(x0)

    for _ in range(mit):
        #si la derivada es nula termino
        if df == 0:
            print("la derivada en el punto es nula")
            break

        xn = x0 - f/df
        f,df = fun(xn)

        hx.append(xn)
        hf.append(f)

        if abs(xn - x0)/abs(xn) < err or abs(f) < err:
            break
        
        x0 = xn    

    return (hx,hf)
