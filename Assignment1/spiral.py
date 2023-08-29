"""
  File: spiral.py
  Description: Function to create a number spiral according to the input dimension and a function to sum the numbers
  surrounding a given number

  Student Name: Quentin Schuelke
  Student UT EID: qcs86 

  Partner Name:
  Partner UT EID:

  Course Name: CS 313E
  Unique Number: 
  Date Created:
  Date Last Modified:

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
    
 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

import math

def print_spiral(spiral):
    for row in range(len(spiral)):
        for col in range(len(spiral)):
            print(spiral[row][col], end="")
            space = " " * (8 - len(str(spiral[row][col])))
            print(space, end="")
        print("\n")
    print()
        


def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""
    side_length = 2
    mid = math.floor(dim/2)
    ring = 1
    # forward = True
    num_to_add = 3

    
        # initialize empty matrix of the given size
    spiral = [0] * dim
    for i in range(dim):
        spiral[i] = [0] * dim
    print_spiral(spiral)

    if dim == 1:
        spiral[0][0] = 1
    else:
        spiral[mid][mid] = 1
        spiral[mid][mid+1] = 2
        print_spiral(spiral)
        while True :
            # bottom
            for col in range(mid+ring, mid+ring-side_length, -1):
                if num_to_add > dim ** 2:
                    break
                spiral[mid-ring][col] = num_to_add
                num_to_add +=1
                print_spiral(spiral)

            # left
            for row in range(mid-ring-1, mid-ring+side_length-1):
                if num_to_add > dim ** 2:
                    break
                spiral[row+1][mid-ring] = num_to_add
                num_to_add +=1

            side_length +=1

            # top
            for col in range(mid-ring, mid-ring+side_length):
                if num_to_add > dim ** 2:
                    break
                spiral[mid+ring][col] = num_to_add
                num_to_add +=1

            # right
            for row in range(mid+ring, mid+ring-side_length, -1):
                if num_to_add > dim ** 2:
                    break
                spiral[row][mid+ring+1] = num_to_add
                num_to_add += 1

            if num_to_add > dim ** 2:
                    break

            side_length +=1
            ring +=1
            print_spiral(spiral)
            print(f"made it to ring {ring}")
        print_spiral(spiral)
        print(spiral)


    



        
  



def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """

    # I think it should just iterate over the rows or columns, then check all the sides
    # set some row and column parameters and an if statement that checks if it's valid 
    
    # ADD YOUR CODE HERE  


    return # ADD YOUR CODE HERE  





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
