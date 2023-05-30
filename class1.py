 

# for i in range(5,10,2):
#     print(i)  

# n = int(input("Enter number"))

# while(n!=0):
#     print(n)
#     if n==3:
#         break

# my_list =[1,3,5,"hello",'hey','mango',4,6]
# print(my_list)
# print(my_list[3])
# print(my_list.index('hello'))
# print(my_list[-2])
# print(my_list[-4])

# print(my_list[1:5:3])
# print(my_list[:])
# print(my_list[::3])
# print(my_list[::-1])

# my_list =[1,3,5,5,6,8,9,4,8]

# for element in my_list:
#     print(element+3)

# for index, element in enumerate(my_list):
#     print(element+index)



# my_list =[1,2,3,4,5,6]
# my_list.append(8)
# my_list.append(4.5)
# print(max(my_list))
# my_list.sort()
# print(my_list)
# print(len(my_list))


matrix_A =[[1,2,3],
           [4,5,6],
           [9,4,6]]
           
matrix_B =[[3,4,5],
           [6,0,1],
           [9,11,2]]
# matrix_C = matrix_A[0][0]+matrix_B[0][0]
# print(matrix_C)
matrix_C =[[0,0,0],
           [0,0,0],
           [0,0,0]]
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        matrix_C[i][j] = matrix_A[i][j]+matrix_B[i][j]
for r in matrix_C:
    print(r)




