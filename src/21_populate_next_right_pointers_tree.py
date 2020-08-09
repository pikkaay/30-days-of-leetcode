'''
Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        queue = [root]
        level = []
        # next_level = []
        root.next = None
        origin = root
        
        while len(queue) > 0:
            # print(queue)
            for root in queue:
                if root.left:
                    level.append(root.left)
                if root.right:
                    level.append(root.right)
            print('')
            print(level)
            if len(level) > 0:
                for i in range(len(level) - 1):
                    level[i].next = level[i+1]
                level[-1].next = None
            queue = level
            level = []
        return origin


'''
Run Code Result:

Your input

[1,2,3,4,5,6,7]
Your stdout


[<__main__.Node object at 0x7fe8e1bbe4c0>, <__main__.Node object at 0x7fe8e0b69070>]

[<__main__.Node object at 0x7fe8e0b691f0>, <__main__.Node object at 0x7fe8e0b698e0>, <__main__.Node object at 0x7fe8e0b69a00>, <__main__.Node object at 0x7fe8e0b69040>]

[]

Your answer

[1,#,2,3,#,4,5,6,7,#]
Expected answer

[1,#,2,3,#,4,5,6,7,#]
'''
