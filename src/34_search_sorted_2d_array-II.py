'''
Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            print('col row', col, row)
            curr = matrix[row][col]
            if target == curr:
                return True
            elif target < curr:
                col -= 1
            elif target > curr:
                row += 1
                
        return False



'''
Run Code Result:

Your input

[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
5
Your stdout

col row 4 0
col row 3 0
col row 2 0
col row 1 0
col row 1 1

Your answer

true
Expected answer

true
'''
