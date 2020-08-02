'''
221. Maximal Square 
 
 
 
 

 
 
 
 

Average Rating: 4.86 (172 votes)

July 14, 2016  |  199.2K views
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
Summary
We need to find the largest square comprising of all ones in the given m \times nm×n matrix. In other words we need to find the largest set of connected ones in the given matrix that forms a square.
'''


def maximalSquare(matrix):
    # handle 0 and 1 dimensional arrays
    if len(matrix) == 0: return 0
    if len(matrix) == 1:
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1': return 1
        return 0
        
    # input array is not guaranteed to be square. use the smallest side for
    # largest possible square
    max_side = len(matrix)
    if max_side > len(matrix[0]): max_side = len(matrix[0])

    # look for largest possible square to smallest 
    for side in reversed(range(0, max_side)):
        for j in range(len(matrix) - side):
            for k in range(len(matrix[j]) - side):
                #print '(' + str(j) + ', ' + str(k) + ') side: ' + str(side + 1)
                if find_square(matrix, j, k, side + 1):
                    return (side + 1)**2
    
    return 0
    
# check a region in the vector for the existence of a square made of '1'
def find_square(matrix, x, y, side):
    if len(matrix) < 2: return False
    if x + side > len(matrix) or y + side > len(matrix[0]): return False
    
    for i in range(x, x + side):
        for j in range(y, y + side):
            if matrix[i][j] == '0': return False

    return True
        

test = [
        "10100",
        "10101",
        "11101",
        "11100",
        "11110"
    ]


# s = Solution()
print ('solution:')
print (maximalSquare(test))
