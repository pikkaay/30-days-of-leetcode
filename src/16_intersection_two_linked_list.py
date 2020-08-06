'''
Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
'''
l1 = ListNode(1)
l1.next = ListNode(2)
intersection = ListNode(3)
l1.next.next = intersection
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

l2 = ListNode(7)
l2.next = ListNode(8)
l2.next.next = ListNode(9)
# l2.next.next.next = intersection

# println(l1), print(''), println(l2)

a_pointer = l1
b_pointer = l2

flag = l1
cycle = 0
while a_pointer != b_pointer:
  if not a_pointer.next:
    cycle += 1
    a_pointer = l2
  else:
    a_pointer = a_pointer.next
    
  if not b_pointer.next:
    print('b none')
    b_pointer = l1
  else:
    b_pointer = b_pointer.next
  print(a_pointer.val, b_pointer.val)
  if cycle > 1:
    break


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA:
            return
        if  not headB:
            return
        
        a_pointer = headA
        b_pointer = headB
        
        cycle = 0
        while a_pointer != b_pointer:
          
          if not a_pointer.next:
            cycle += 1
            print('a none')
            a_pointer = headB
          else:
            a_pointer = a_pointer.next
            
          if not b_pointer.next:
            print('b none')
            b_pointer = headA
          else:
            b_pointer = b_pointer.next
          print(a_pointer.val, b_pointer.val)
          if cycle > 1:
                return
        return a_pointer

'''
Run Code Result:

Your input

8
[4,1,8,4,5]
[5,6,1,8,4,5]
2
3
Your stdout

1 6
8 1
4 8
5 4
a none
5 5
b none
6 4
1 1
8 8

Your answer

Intersected at '8'
Expected answer

Intersected at '8'
Show Diff
Runtime: 28 ms
'''
