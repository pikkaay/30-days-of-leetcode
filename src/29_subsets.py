'''
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, result, [], 0)
        return result
    
    def helper(self, nums, result, current, index):
        result.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.helper(nums, result, current, i+1)
            current.pop()



'''
Run Code Status: Finished

×
Run Code Result:

Your input

[1,2,3]
Your answer

[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
Expected answer

[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''


# non-recursive
# Simple and short

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        if len(nums) == 0:
            return result
        for item in nums:
            result += [lst + [item] for lst in result]
        return result
