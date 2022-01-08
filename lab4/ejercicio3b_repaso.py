import numpy as np
test = [1,2]


K = 5
N = 10
matrix_result = np.zeros(N)
for idx in range (0,K):
    a_np = np.arange((N*N))
    print(a_np)

    matrix_result[idx] = a_np.reshape(N,N)




print(test)