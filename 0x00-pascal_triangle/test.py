# usr/bin/python3
def pascal_triangle(n):
    """
        A function that returns a list of lists of integers representing 
        the Pascal’s triangle of n. It returns an empty list if n <= 0
    """
    matrix = [] # A list of lists or outer list
    for i in range(n):
        innerList = [] #  Create an inner list 
        for j in range(i + 1):
            if j == 0 or j == i:  # First and last elements are always 1
                innerList.append(1)
            else:
                # Sum the two elements from the previous row
                innerList.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        
        matrix.append(innerList) # Append the inner list to matrix
    
    # Printing the result
    for row in matrix:
        print(row)