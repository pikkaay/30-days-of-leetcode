'''
 Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        chset = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = ['']
        for digit in digits:
          result = self.update_result(digit, result, chset)
        return result
    
    def update_result(self, digit, result, chset):
      new_result = []
      for item in result:
        for character in chset[int(digit)]:
          new_result.append(item + character)
      return new_result

'''
Run Code Result:

Your input

"23"
Your answer

["ad","ae","af","bd","be","bf","cd","ce","cf"]
Expected answer

["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''
