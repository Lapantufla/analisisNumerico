# cada kg de fertilizante cubre para 10m**2 
# el fertilizante debe contener almenos : 3g de P, 1.5g de N y 4g de K por cada 10m**2
# 
# fertizante  T1   -   T2 - 
#      N    | 1g    |3g     |   
#      P    | 3g    |2g     | 
#      K    | 8g    |2g     |
# costo :   $10     |$8
# 
# A = cantidad de fertilizante de T1
# B = cantidad de fertilizante de T2
# 
# => tenemos que la funcion a minimizar es 10*A + 8*B
#                                  s/a   1*A + 3*B >= 1.5 (N)
#                                        3*A + 2*B >= 3 (P)   
#                                        8*A + 2*B >= 4 (K)    
#  #