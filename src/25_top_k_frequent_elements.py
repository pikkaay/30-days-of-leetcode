'''
Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        table = {}
        for item in nums:
            if not item in table:
                table[item] = 1
            else:
                table[item] += 1
        keys = [key for key, value in table.items()]
        values = [value for key, value in table.items()]
        print(keys, values)
        
        result = []
        for _ in range(k):
            large = float('-inf')
            for i in range(len(values)):
                if values[i] > large:
                    large = values[i]
                    index = i
            
            result.append(keys[index])
            keys.pop(index)
            values.pop(index)
        print(result)
        return result


'''
Run Code Status: Finished

×
Run Code Result:

Your input

[1,1,1,2,2,3]
2
Your stdout

[1, 2, 3] [3, 2, 1]
[1, 2]

Your answer

[1,2]
Expected answer

[1,2]
'''
