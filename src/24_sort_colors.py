'''
ort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        count = [0,0,0]
        for item in nums:
            if item == 0:
                count[0] += 1
            elif item == 1:
                count[1] += 1
            else:
                count[2] += 1
        print('count', count)
        color = pointer = 0
        while count != []:
            c = count.pop(0)
            print('c', c)
            if c > 0:
                for i in range(pointer , pointer + c):
                    print('i',i)
                    nums[i] = color
                pointer += c
            color += 1
            print('pointer', pointer)


'''
Run Code Result:

Your input

[2,0,2,1,1,0]
Your stdout

count [2, 2, 2]
c 2
i 0
i 1
pointer 2
c 2
i 2
i 3
pointer 4
c 2
i 4
i 5
pointer 6

Your answer

[0,0,1,1,2,2]
Expected answer

[0,0,1,1,2,2]
'''
