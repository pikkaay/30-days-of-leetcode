'''
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        rows = len(board)
        columns = len(board[0])
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0] and self.helper(board, word, 0, i, j):
                    print(i, j)
                    return True
        return False
    
    def helper(self, board, word, index, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
        or board[i][j] != word[index]:
            return False
        if index == len(word)-1:
            return True
        seen = board[i][j] 
        board[i][j] = '##'
        if self.helper(board, word, index+1, i+1, j) or \
        self.helper(board, word, index+1, i, j+1) or \
        self.helper(board, word, index+1, i-1, j) or \
        self.helper(board, word, index+1, i, j-1):
            return True
        board[i][j]  = seen
        return False
'''
Run Code Status: Finished

Run Code Result:

Your input

[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
Your stdout

0 0

Your answer

true
Expected answer

true
'''
        