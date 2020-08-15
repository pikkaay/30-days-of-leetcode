'''
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

intervals[i][0] <= intervals[i][1]
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []
        i = 0
        self.mergeSort(intervals)
        print(intervals)
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = intervals[i +1][1]
                print(intervals[:i+1])
                print(intervals[i+1:])
                # if i < len(interval)
                intervals = intervals[:i+1] + intervals[i+2:]
            i += 1
        return intervals
    
    def mergeSort(self, arr):
        if len(arr)<2:
          return
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
  
        self.mergeSort(L)
        self.mergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i][0] == R[j][0]:
                arr[k] = L[i]
                i += 1
            elif L[i][0] < R[j][0]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
'''
Run Code Result:

Your input

[[1,3],[2,6],[8,10],[15,18]]
Your stdout

[[1, 3], [2, 6], [8, 10], [15, 18]]
[[1, 6]]
[[2, 6], [8, 10], [15, 18]]

Your answer

[[1,6],[8,10],[15,18]]
Expected answer

[[1,6],[8,10],[15,18]]
'''
