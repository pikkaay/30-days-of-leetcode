'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


def threeSum(nums):
    nums.sort()
    triplet = []
    
    print(nums)
    for i in range(len(nums) - 2):
        
        if i > 0 and nums[i] == nums[i - 1]: continue
        print('i', i)

        left = i + 1
        right = len(nums) - 1
        print('i, left, right', i, left, right)
        while left < right:
            
            currentsum = nums[i] + nums[left] + nums[right]
            if currentsum == 0:
                triplet.append([nums[i], nums[left], nums[right]])
                
                print('x', nums[left], nums[left + 1])
                while left < right and nums[left] == nums[left + 1]:
                    print('x', i, left, right)
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif currentsum < 0:
                left += 1
            
            else:
                right -= 1
    return triplet
                
# [-4, -1, -1, 0, 1, 2]


arr = [-1, 0, 1, 2, -1, -4]
print(threeSum(arr))

'''
[-4, -1, -1, 0, 1, 2]
i 0
i, left, right 0 1 5
i 1
i, left, right 1 2 5
x -1 0
x 0 1
i 2
i, left, right 2 3 5
x 0 1
i 3
i, left, right 3 4 5
[[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]]
'''
