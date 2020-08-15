'''
Search for a Range

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if len(nums) == 0:
            return result
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        print('left', left)
        print(nums[left])
        if nums[left] != target:
            return result
        result[0] = self.left_index(nums, left, target)
        result[1] = self.right_index(nums, left, target)
        return result
    
    def left_index(self, nums, index, target):
        for i in range(index, 0):
            if nums[i] != target:
                print('left', i)
                return i+1
            if num[i] == target:
                return i
        return index
    def right_index(self, nums, index, target):
        for i in range(index, len(nums)):
            print(i)
            if nums[i] != target:
                return i-1
        if nums[i] == target:
            return i
        return index


'''
Run Code Result:

Your input

[5,7,7,8,8,10]
8
Your stdout

left 3
8
3
4
5

Your answer

[3,4]
Expected answer

[3,4]
'''

