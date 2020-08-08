'''
 Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if self.allupper(word):
            return True
        
        if self.alllower(word):
            return True        
        
        if word[0].isupper():
            if self.allupper(word[1:]):
                return True
            if self.alllower(word[1:]):
                return True
    
    def allupper(self, string):
        for i in range(len(string)):
            if string[i].islower():
                return False
        return True
    
    def alllower(self, string):
        for i in range(len(string)):
            if string[i].isupper():
                return False
        return True


'''
Run Code Status: Finished

×
Run Code Result:

Your input

"USA"
Your answer

true
Expected answer

true
'''
