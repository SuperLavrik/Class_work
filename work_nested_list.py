import random
import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = 3
M = 5
#matrix =[[0] * N] * M                   # сформирована 1 строка из Н  0 и продублирована М раз

row = [0] * N
for _ in range(M):
    matrix. append(row[:])


#print (len(matrix))
def initialize_matrix(matrix, lower_bound, upper_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
             matrix[i][j] = random.randint(lower_bound, upper_bound)
    return



def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
             print(matrix[i][j], end="\t")
        print()
    return



initialize_matrix(matrix,10, 100)
print_matrix(matrix)

# def multiply_matrix_by_n(matrix, n):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#              matrix[i][j] *= n
#     return
#
# print()
# multiply_matrix_by_n(matrix, 10)
# print_matrix(matrix)




