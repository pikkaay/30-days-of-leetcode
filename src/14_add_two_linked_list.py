'''








'''
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
# l2.next.next.next = ListNode(5)

carry = 0
ln = ListNode()
dummy = ListNode()
dummy.next = ln
print(l1.val, l2.val, ln.val)
while l1 or l2 or carry > 0:
    
    if not l1 : val1 = 0
    else: val1 = l1.val
    
    if not l2: val2 = 0
    else: val2 = l2.val
    
    print('val1, val2', val1, val2)
    sm = val1 + val2 + carry
    sm_val = sm % 10
    carry = sm //10

    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next
    
    ln.val = sm_val
    if l1 or l2 or carry > 0:
      ln.next = ListNode()
      ln = ln.next

ln = dummy.next

while ln:
  print(ln.val)
  ln = ln.next
