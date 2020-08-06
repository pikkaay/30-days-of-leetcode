'''
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''

[1, 2, 3, 4, 5]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


odd = head
even_head = head.next
even = head.next

while even and even.next:
  print(odd.val, even.val, odd.next.val, even.next.val)
  odd.next = even.next
  odd = odd.next
  even.next = odd.next
  even = even.next

odd.next = even_head
return head

while head:
  print(head.val)
  head = head.next
