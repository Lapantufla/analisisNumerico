
def horn(coefs,x):
    n = len(coefs)
    b = coefs[0]

    for i in range(1,n):
        b = coefs[i] + x * b
    return b

