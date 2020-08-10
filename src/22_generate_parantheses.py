'''
  Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(result, '', n, n)
        return result
    
    def helper(self, result, current, left, right):
        if left < 0 or left > right:
            return
        if left == 0 and right == 0:
            result.append(current)
        self.helper(result, current + '(', left-1, right)
        self.helper(result, current + ')', left, right-1)
        return


'''
Run Code Status: Finished

×
Run Code Result:

Your input

3
Your answer

["((()))","(()())","(())()","()(())","()()()"]
Expected answer

["((()))","(()())","(())()","()(())","()()()"]
'''
