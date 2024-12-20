#Q.2
import numpy as np

x_1 = 1
x_2 = 1

matrix = np.array([[ 2, 4, -4 ],
                   [ 5, 7, 11 ]])

copy_matrix = matrix.copy()

def solve_P1_2(copy_matrix):
    
    print(f"Our original augmented matrix is:\n {copy_matrix}\n")
    print("The first operation we'll do is multiply row 1 by 1/2 to isolate x1\n")
    copy_matrix[0] = (1/2) * matrix[0]
    
    
    print(f"Now our matrix is:\n {copy_matrix}\n")
    
    print(f"Now lets perform a replacement operation on row 1 (0-indexed)")
    
    copy_matrix[1] = (-5 * copy_matrix[0]) + copy_matrix[1]
    
    print(f"Now our new triangular augmented matrix is:\n {copy_matrix}\n")
    print("Now lets multiply row 1(0-indexed) by -(1/3) and get our solution for x2 ")
    
    copy_matrix[1] = -(1/3) * copy_matrix[1]
    print(f"After the operation our matrix is : \n {copy_matrix}\n")
    print("Now lets get rid of 2 in row 0 by the replacement operation")
    
    copy_matrix[0] = (-2 * copy_matrix[1]) + copy_matrix[0]
    print(f"Now our matrix is: \n{copy_matrix}\n")
    
    print(f"So our official solution set is (x1 : {copy_matrix[0][2]}, x2 : {copy_matrix[1][2]})")
    
    print("Now lets verify our solution set")
    x_1 = copy_matrix[0][2]
    x_2 = copy_matrix[1][2]
    
    row_1_verify = (matrix[0][0] * x_1) + (matrix[0][1] * x_2)
    row_2_verify = (matrix[1][0] * x_1) + (matrix[1][1] * x_2)
    print(row_1_verify)
    print(row_2_verify)
    
    
    if row_1_verify == -4 and row_2_verify == 11:
        print("True")
    else:
        print("False")
    
    
    

solve_P1_2(copy_matrix)