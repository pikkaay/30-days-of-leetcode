'''
This is pure magic

'''

# not working solution

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         table = []
#         self.helper(nums, table, result)
#         return result
    
#     def helper(self, nums, table, result):
#         if len(nums) == 0:
#             result.append(table)
        
#         for i in range(len(nums)):
#             newNums = nums[0:i] + nums[i+1:]
#             table.append(nums[i])
#             self.helper(newNums, table, result)
#             table.pop()
#             print(table)
        
#         return result



# approach 2


def permutation(nums):
	print('nums', nums)
	if len(nums) == 0:
		return []
	if len(nums) == 1:
		return [nums]
	else:
		ls = []
		for i in range(len(nums)):
			x = nums[i]
			xs = nums[:i] + nums[i+1:]
			print('x', x)
			print('xs', xs)
			for p in permutation(xs):
				print('p', p)
				ls.append([x] + p)
				print('ls', ls)
			print('lse', ls)
		return ls

print(permutation([1,2, 3]))
