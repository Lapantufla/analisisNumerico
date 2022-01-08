def trapecio(fun, a, b, N):
    h = (b - a)/ N
    result_of_summation = 0
    result_of_parenthesis = 0
    
    for j in range(1, N):
        result_of_summation += fun(a + j * h)

    result_of_parenthesis = fun(a) + 2 * result_of_summation + fun(b)
    return( h/2 * result_of_parenthesis )
