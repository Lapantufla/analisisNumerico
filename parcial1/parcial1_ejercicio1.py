""" 
#use la sig funcion para corroborar que el metodo ande bien
def fun_quad(x):
    return x**2 - 2
"""

def swap(a, b):
    aux = a
    a = b 
    b = aux 

    return (a,b)


def rsecante(fun, x0, x1, err, mit):
  
    hx = []
    hf = []
    a = x0
    b = x1
    
    fa = fun(a)
    fb = fun(b)
    """ 
    hago estas indexaciones aca ya que en el cuerpo del for no podria, 
    queda medio feo pero no se me ocurrio otra forma
    """
    hx.append(b)
    hf.append(fb)
    
    hx.append(a)
    hf.append(fa)
    
    for _ in range(mit - 2):
        if abs(fa) > abs(fb):
            swap(a, b)

        part_adding = (a - b) / (fa - fb)
        b = a
        fb = fa 

        a = a - (fa * part_adding)
        fa = fun(a)

        hx.append(a)
        hf.append(fa)

        if abs(fa) < err:
            break
    
    return (hx,hf)

""" 
#use el sig ejemplo para corroborar que el metodo ande
hx, hf = rsecante(fun_quad, 4, 5, 1e-5, 100)
print(hx,hf)
"""