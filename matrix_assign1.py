
matrix_A =[[1,2,3],
           [4,5,6],
           [9,4,6]]
           
matrix_B =[[3,4,5],
           [6,0,1],
           [9,11,2]]

matrix_C =[[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        matrix_C[i][j] = matrix_A[i][j]+matrix_B[i][j]
        
for r in matrix_C:
    print(r)