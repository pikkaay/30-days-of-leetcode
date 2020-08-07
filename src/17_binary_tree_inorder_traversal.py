'''
Binary Tree Inorder Traversal

Solution
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.traversal(root)
    
    def traversal(self, root):
        if not root:
            return []
        return self.traversal(root.left) + [root.val] +  self.traversal(root.right)
        

'''
Your input

[1,null,2,3]
Your answer

[1,3,2]
Expected answer

[1,3,2]
'''
