from practico2_ejercicio3 import rnewton

#preguntar lunes
#es como una variable global?¿?
numeroA = int(input("ingrese un numero positivo: "))

def funcion_prueba(x):
    f = ( x ** 3) - numeroA
    df = 3 * (x ** 2)
    
    return (f,df) 


def funcion_main():
    if(numeroA < 0):
        print("El numero ingresado no es positivo, porfavor intente nuevamente")
        return None    
    hx, hf = rnewton(funcion_prueba, 1, 1e-4, 100)
    print(hx, hf)

funcion_main()