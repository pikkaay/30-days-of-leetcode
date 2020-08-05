'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
''' 

nums = [1, 2, 1, 0, 4]


def fn(nums):
	small = float('inf')
	big = float('inf')
	for item in nums:
		if item <= small:
			small = item
		elif item <= big:
			big = item
		else:
			return True
	return False

print(fn(nums))

'''
debug

[1, 2, 1, 0, 4]

loop 1:
item = 1
small = inf
big = inf
if item <= small : if 1 < inf : yes
small = 1

loop2:
item = 2
small = 1
big = inf
if item <= small : if 2 <= 1 : no
elif item <= big : if 2 <= inf : yes
big = 2

loop3:
item = 1
small = 1
big = 2
if item <= small : if 1 <= 1 : yes
small  = 1

loop4:
item = 0
small = 1
big = 2
if item <= small : if 0 <= 1 : yes
small = 0

loop5:
item = 4
small = 0
big = 2
if item <= small : if 4 <= 0 : no
elif item <= big : if 4 <= 2 : no
return True

==================
[1, 2, 1, 0, 2]

loop5:
item = 2
small = 0
big = 2
if item <= small : if 2 <= 0 : no
elif item <= big : if 2 <= 2 : yes
big = 2
return False

==================
[1, 2, 1, 0, 3]

loop5:
item = 3
small = 0
big = 2
if item <= small : if 2 <= 0 : no
elif item <= big : if 3 <= 2 : no
return True

'''
