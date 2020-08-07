'''
Kth Smallest Element in a BST


Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
   Hide Hint #1  
Try to utilize the property of a BST.
   Hide Hint #2  
Try in-order traversal. (Credits to @chan13)
   Hide Hint #3  
What if you could modify the BST node's structure?
   Hide Hint #4  
The optimal runtime complexity is O(height of BST).

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    return traversal(root)

def traversal(root):
    if not root:
        return []
    return traversal(root.left) + [root.val] +  traversal(root.right)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return
        a_pointer = root
        b_pointer = root
        count = 1
        while True:
            b_pointer = b_pointer.left
            if b_pointer is None:
                ls = inorderTraversal(a_pointer)
                ls.sort()
                return ls[k-1]
            if count >= k:
                a_pointer = a_pointer.left
            count += 1
            
