'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    idict = set()
    jdict = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                idict.add(i)
                jdict.add(j)
    print(idict)
    print(jdict)

    for i in idict:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for i in jdict:    
        for j in range(len(matrix)):
            matrix[j][i] = 0


matrix = [
[1,1,1],
[0,1,1],
[1,1,1]]
# setZeroes(matrix)
# print(matrix)

'''
[
[0, 1, 1], 
[0, 0, 0], 
[0, 1, 1]]


[
[1, 1, 1], 
[0, 0, 0], 
[1, 1, 1]]
'''

##################################################################################
# O(1) Space 

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # Handle first row and column
    firstcol = firstrow = False
    for i in range(len(matrix)):
      if matrix[i][0] == 0:
        firstcol = True
        break

    for i in range(len(matrix[0])):
      if matrix[0][i] == 0:
        firstrow = True
        break

    print(firstcol, firstrow)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
              matrix[i][0] = 0
              matrix[0][j] = 0

    print(matrix)
    for i in range(1, len(matrix)):
      if matrix[i][0] == 0:
        for j in range(len(matrix[0])):
          matrix[i][j] = 0

    for i in range(1, len(matrix[0])):
      if matrix[0][i] == 0:
        for j in range(len(matrix)):
          matrix[j][i] = 0

    if firstcol:
      for i in range(len(matrix)):
        matrix[i][0] = 0

    if firstrow:
      for i in range(len(matrix[0])):
        matrix[0][i] = 0


matrix = [
[1,1,1],
[1,1,0],
[1,1,1]
]


matrix = [
[0,1,2,0],
[3,4,5,2],
[1,3,1,5]]
setZeroes(matrix)
print(matrix)


'''
[
[0, 0, 0, 0], 
[0, 4, 5, 0], 
[0, 3, 1, 0]]


'''
