#practico 1
import math;
import random;


def multiplo(n,m):
    if n % m == 0:
        print("Es divisible")
        return True
    else:
        print("No es divisible")
        return False


#ejercicio 2
""" a = 1 + (pow(2,-53))
print("el valor de a es:", a)

b = 1 + (pow(2,-52))
print("el valor de b es:", b) """

#ejercicio 3
def detect_overflow (n):
    while  math.isinf(n * 2) != True:
        n = n * 2
    print("Para overflow, el valor de n es:", n )   


def detect_underflow (m):
    while  math.isinf(m / 2) != True:
        m = m / 2
    print("Para underflow, el valor de n es:", m )   



#ejercicio 5
def faq_six(n):
    if n == 0:
        return 1
    aux = 1
    for i in range(1,n+1):
        aux = aux * i
    result = aux
    return result
#print("El resultado es %i" %faq_six(0))        

#ejercicio6
def is_greater_than ():
    numero1 = float(input("Ingrese un numero real: "))
    numero2 = float(input("Ingrese otro numero real: "))

    if numero1 > numero2:
        return print("El numero %f es el mayor" %numero1)
    elif numero1 == numero2:
        return print("%f es igual a %f" %(numero1, numero2))
    else:
        return print("El numero %f es el mayor" %numero2)   

#ejercicio7
def power_n(base, exponente):
    if exponente == 0:
        return 1
    aux = base    
    for i in range(1, exponente):
        aux = aux * base
    result = aux
    return result

def first_five_power ():
    numeroBase = int(input("Ingrese el numero que desea potenciar: "))
    numeroExponente = int(input("Ingrese la potencia de dicho numero: "))

    return power_n(numeroBase, numeroExponente)

#print("El resultado es : %i" % first_five_power())

#ejercicio8
def mala(a, b, c):
    disc = b**2 - 4 * a * c

    if disc < 0:
        print("El discriminante es negativo")
        return None
    
    x_1 = (-b + sqrt(disc))/(2.0 *a)
    x_2 = (-b - sqrt(disc))/(2.0 *a)

    return [x_1, x_2]

def buena(a, b, c):
    disc = b**2 - 4 * a * c
#econtrar la raiz mas lejana al cero en valor absoluto
    if b > 0:
        x_1 = (-b - sqrt(disc))/(2.0 *a)
    else :
        x_1 = (-b + sqrt(disc))/(2.0 *a)
    
    x_2 = (c / a) / x_1
    return [x_1, x_2]

#ejercicio9
def horn(coefs,x):
    n = len(coefs)
    b = coefs[0]

    for i in range(1,n):
        b = coefs[i] + x * b
    return b
p = horn([1,2,3], 2)
print(p)

#ejercicio10
def sonReciprocos(x,y):
    if int(x) == 0 | int(y) == 0:
        print("Error cero no tiene reciproco")
        return None
    
    if int(x * y) == 1:
        return True
    else:
        return False


