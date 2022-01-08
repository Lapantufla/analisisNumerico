
def rbisec (fun, I, err, mit):
    a = I[0]
    b = I[1]
    
    if a >= b:
        #el intervalo de input debe estar ordenado de menor a mayor ie a < b
        return None
    if fun(a) * fun(b) >= 0:
        #tienen igual signo, el metodo no puede ejecutarse
        return None

    
    hx = []
    hf = []  

    for it in range(mit):
        c = (a + b) / 2
        fun_evaluado_c  = fun(c)

        #append es para enlistar
        hx.append(c)
        hf.append(fun_evaluado_c)

        if abs(fun_evaluado_c) < err:
            break

        if fun_evaluado_c * fun(a) < 0:
            b = c

        else:    
            a = c
            
    return (hx, hf)