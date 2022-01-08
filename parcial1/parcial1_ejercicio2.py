from parcial1_ejercicio1 import rsecante
from rnewton_aux import rnewton

def fun_square_2(x):
    return (x**2 - 2, 2*x)

def busqueda_ceros(fun, x0, x1, err, mit):

    #hago esta funcion lambda para poder pasarsela a rsecante ya que esta no necesita la derivada
    fun_prima = lambda x : fun(x) [0]

    hx_secant, hf_secant = rsecante(fun_prima, x0, x1, err, mit)
    hx_newton, hf_newton = rnewton(fun, x0, err, mit)

    #print("las iteraciones en X con el metodo de la secante: ", hx_secant)
    #print("las iteraciones en f(x) con el metodo de la secante: " , hf_secant)

    #print("las iteraciones en X con el metodo de la newton: ", hx_newton)
    #print("las iteraciones en f(x) con el metodo de la newton: " , hf_newton) 

    #cantidad iteraciones para llegar al "cero"
    iterations_secant = len(hx_secant)
    iterations_newton = len(hx_newton)
    print("El metodo de la Secante hace una cantidad de %i iteraciones" % iterations_secant)
    print("El metodo de Newton hace una cantidad de %i iteraciones" %iterations_newton)

    #los ceros encontrados
    cero_secant = hx_secant[-1]
    cero_newton = hx_newton[-1]
    print("El cero encontrado por el metodo de la Secante es: " , cero_secant)
    print("El cero encontrado por el metodo de Newton es: " , cero_newton)
    
    
    #verifico cual es la mejor solucion 
    if abs(hf_newton[-1]) < abs(hf_secant[-1]):
        return cero_newton
    else:
        return cero_secant
    
#para correr descomentar : 
#busqueda_ceros(fun_square_2, 4.0, 5.0, 1e-7, 100)