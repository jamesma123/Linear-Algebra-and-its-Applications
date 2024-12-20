#Q.1
'''import numpy as np

matrix = np.array([[1,5,7],[-2,-7,-5]])
origin = matrix.copy()
print(matrix)


def solveP1_1(matrix):
    
    origin[1] = (2 * origin[0]) + origin[1]
    print(f"After the first replacement operation we get {origin}")
    
    origin[1] = (1/3) * origin[1]
    print(f"After the next replacement operation, the matrix is now {origin}")
    
    print("So this gives us x2 = 3 which I will now substitute back into the original equation")
    
    x_2 = 3
    print(f"after setting our varaible for x2, we use it to sub into row 0 and find x1")
      
    origin[0][1] *= x_2
    
    origin[0][2] -= origin[0][1]
    origin[0][1] = 0
    
    print(origin)
    
    print(f"So our solution set should come out to ({origin[0][2]},{origin[1][2]})")
    
    x_0 = origin[0][2]
    x_1 = origin[1][2]
    print(x_0)
    print(x_1)
    print(origin[0])
    print(origin[1])
    
    origin[0] = (origin[0][0] * x_0) + (5 * x_1)
    origin[1] = (origin[1][0] * x_0) - (-7 * x_1)
    
    print(origin)
    print(matrix)
    
    
    
solveP1_1(origin)
'''

import numpy as np

# Define the matrix
matrix = np.array([[1, 5, 7], [-2, -7, -5]])

def solveP1_1(matrix):
    # Create a copy to avoid modifying the original matrix
    origin = matrix.copy()
    print("Original Matrix:")
    print(origin)

    # Step 1: Perform the first row operation: R2 = 2*R1 + R2
    origin[1] = 2 * origin[0] + origin[1]
    print("\nAfter row operation R2 = 2*R1 + R2:")
    print(origin)

    # Step 2: Scale the second row: R2 = (1/3)*R2
    origin[1] = (1/3) * origin[1]
    print("\nAfter scaling R2 = (1/3)*R2:")
    print(origin)

    # Step 3: Back substitution to find x1
    x2 = origin[1][2]
    x1 = origin[0][2] - origin[0][1] * x2
    origin[0][1] = 0  # Clear the modified entry for clarity

    print("\nAfter back substitution:")
    print(origin)
    print(f"Solution: x1 = {x1}, x2 = {x2}")

    # Verification step (optional)
    print("\nVerification:")
    print(f"Row 1: {origin[0][0]}*x1 + {origin[0][1]}*x2 = {origin[0][2]}")
    print(f"Row 2: {origin[1][0]}*x1 + {origin[1][1]}*x2 = {origin[1][2]}")
    print(matrix)
    print(x1)
    print(x2)
    
    print(f"{(matrix[0][0] * x1) + (matrix[0][1] * x2)}")
    print(f"{(matrix[1][0] * x1) + (matrix[1][1] * x2)}")

# Solve the problem
solveP1_1(matrix)
